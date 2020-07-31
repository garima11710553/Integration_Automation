from pathlib import Path
import subprocess
import json

''' इधर तो देखो '''

doing_precision_reduction = False
doing_key_changing = True
doing_minify_of_json = True
doing_plist_to_json = False
doing_deletion_of_keys = False
precision_up_to = 4

''''''''''''''''''''''''''''''


deletion_keys = [
    "NORMALIZED_CONTENT_OFFSET"
]

old_keys_mapped_to_new_keys ={
	'CIPFA': 'CollageIsPremiumFeatureApplied',
	'CLD': 'CollageLayoutDescription',
	'CSA': 'CollageStateAspect',
	'CSBCo': 'CollageStateBColor',
	'CSCo': 'CollageStateGColor',
	'CSGCo': 'CollageStateGColorSecond',
	'CSIB': 'CollageStateInnerB',
	'CSIR': 'CellStateImageRotation',
	'CSISL': 'CollageStateIsShapeLayout',
	'CSIZ': 'CollageStateIsZorder',
	'CSLT': 'CollageStateLayoutTag',
	'CSOS': 'CollageStateOpacityShadow',
	'CSOB': 'CollageStateOuterB',
	'CSRM': 'CollageStateRoundM',
	'CSSB': 'CollageStateShadowBlur',
	'CSSCo': 'CollageStateShadowColor',
	'CSXOS': 'CollageStateXOffsetShadow',
	'CSYOS': 'CollageStateYOffsetShadow',
	'CSD': 'CollageStickerDescription',
	'CStA': 'CollageStyleApplied',
	'CTD': 'CollageTextDescription',
	'CSPat': 'CollageStatePattenImage',
	'CSS': 'CollageStateSticker',
	'SSNCF': 'StickerStateNCFrame',
	'SPanP': 'StickerStatePreviousPanPoint',
	'SSPR': 'StickerStatePreviousRotation',
	'SSPS': 'StickerStatePreviousScale',
	'SSRA': 'StickerStateRotationAngle',
	'SSSCL': 'StickerStateScale',
	'SCusS': 'StickerStateStickerCustomSticker',
	'SSSt': 'StickerStateStyle',
	'SSZ': 'StickerStateZorder',
	'CST': 'CollageStateText',
	'TSA': 'TextStateAlignment',
	'TSCo': 'TextStateColor',
	'B': 'B',
	'G': 'G',
	'R': 'R',
	'TSCI': 'TextStateColorIdentifier',
	'TSC': 'TextStateContent',
	'TSF': 'TextStateFont',
	'TSMD': 'TextStateIsModelDirty',
	'TSNCF': 'TextStateNCFrame',
	'TSO': 'TextStateOpacity',
	'TSPanP': 'TextStatePreviousPanPoint',
	'TSPR': 'TextStatePreviousRotation',
	'TSPS': 'TextStatePreviousScale',
	'TSRA': 'TextStateRotationAngle',
	'TSS': 'TextStateScale',
	'TSSCo': 'TextStateStrokeColor',
	'TSSW': 'TextStateStrokeWidth',
	'TSSt': 'TextStateStyle',
	'TSZ': 'TextStateZorder',
	'CSGC': 'CollageStateGCells',
	'CSBF': 'CellStateBackgroundFlag',
	'CSMask': 'CellStateCellMask',
	'P0x': 'POINT0x',
	'P0y': 'POINT0y',
	'TP': 'TYPE',
	'P1x': 'POINT1x',
	'P1y': 'POINT1y',
	'P2x': 'POINT2x',
	'P2y': 'POINT2y',
	'P3x': 'POINT3x',
	'P3y': 'POINT3y',
	'P4x': 'POINT4x',
	'P4y': 'POINT4y',
	'P5x': 'POINT5x',
	'P5y': 'POINT5y',
	'P6x': 'POINT6x',
	'P6y': 'POINT6y',
	'CSNCF': 'CellStateNCFrame',
	'h': 'h',
	'w': 'w',
	'x': 'x',
	'y': 'y',
	'CSRA': 'CellStateRotationAngle',
	'CSVIS': 'CellStateSuperViewIndexOfSubview',
	'CSVP': 'CellStateViewProps',
	'ZScl': 'ZOOM_SCALE',
	'CSZ': 'CellStateZorder',
	'GCM': 'gridCellMirror',
	'GCS': 'gridCellSync',
	'GCT': 'gridCellType',
	'GCV': 'gridCellVector'
}

rounding_allowed_for_all_float_vals = True


def round_the_val(val):
    val = round(val, precision_up_to)
    if val == int(val):
        return int(val)
    return val


def plist_to_json(plist_file_path, delete_old_plist_file=True):
    converting_os_cmnd = f"plutil -convert json {plist_file_path} -e json"
    ret = subprocess.run(converting_os_cmnd.split(' '))
    if ret.returncode != 0:
        print(ret.returncode)
        print(
            f"{plist_file_path} is a empty plist file, maiking corresponding empty json file")
        with open(plist_file_path.replace('.plist', '.json'), 'w') as f:
            f.write('{}')
    if delete_old_plist_file:
        removing_file_cmnd = f"rm {plist_file_path}"
        subprocess.run(removing_file_cmnd.split(' '))
    return


def iterate_and_make_changes(mapping_val, parent=None, val_keys=None):
    if isinstance(mapping_val, float):
        if doing_precision_reduction and \
            ((parent != None and val_keys != None and parent in val_keys) or
                rounding_allowed_for_all_float_vals):
            return round_the_val(mapping_val)
        return mapping_val

    if isinstance(mapping_val, dict):
        keys = list(mapping_val.keys())
        for key in keys:
            mapping_val[key] = iterate_and_make_changes(
                mapping_val[key], key, val_keys=val_keys)
            if doing_key_changing and key in old_keys_mapped_to_new_keys:
                new_key = old_keys_mapped_to_new_keys[key]
                mapping_val[new_key] = mapping_val[key]
                if new_key != key:
                    del mapping_val[key]
            if doing_deletion_of_keys and key in deletion_keys:
                del mapping_val[key]

    if isinstance(mapping_val, list):
        for i in range(len(mapping_val)):
            mapping_val[i] = iterate_and_make_changes(
                mapping_val[i], parent, val_keys=val_keys)

    return mapping_val


def reduce_size_of_json_file(input_file_path, output_file_path=None):
    if not input_file_path.endswith('.json'):
        print(f"{input_file_path} is not a json file")
        return
    if output_file_path == None:
        output_file_path = input_file_path

    with open(input_file_path, 'r') as f:
        mapping_val = json.loads(f.read())
    mapping_val = iterate_and_make_changes(mapping_val)
    with open(input_file_path, 'w') as f:
        if doing_minify_of_json:
            f.write(json.dumps(mapping_val, separators=(',', ':')))
        else:
            f.write(json.dumps(mapping_val, indent=3, sort_keys=True))
    return


def print_msg(file_path):
    global c
    print(f"This {file_path} has been changed")
    c=c+1
    return


def do_change_in_all_files_within_folder_iteratively(folder_path):
    json_files = Path(folder_path).glob('**/*.json')
    for json_file in json_files:
        file_path = str(json_file)
        print_msg(file_path)
        reduce_size_of_json_file(file_path)
    if doing_plist_to_json:
        plist_files = Path(folder_path).glob('**/*.plist')
        for plist_file in plist_files:
            file_path = str(plist_file)
            plist_to_json(file_path)
            print_msg(file_path)
            reduce_size_of_json_file(file_path.replace('.plist', '.json'))
    return

def function_for_psx_json_change():
    
    folder_to_change = "/Users/garimsin/Documents/Integration/Server Upload 2/demo_layouts_data"
    do_change_in_all_files_within_folder_iteratively(folder_to_change)
c=0
function_for_psx_json_change()
print(c)
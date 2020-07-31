import json, sys, os

def bound(mask_points, frame,):
    x, y, h, w = frame['x'], frame['y'], frame['h'], frame['w']
    maxx, minx, maxy, miny = sys.float_info.min, sys.float_info.max , sys.float_info.min , sys.float_info.max
    for point in mask_points:
        flag = False
        for k,v in point.items():
            if k.endswith('x'):
                flag = True
                v = x + v * w
                maxx = max(maxx, v)
                minx = min(minx, v)
                point[k] = v
            elif k.endswith('y'):
                flag = True
                v = y + v * h
                maxy = max(maxy, v)
                miny = min(miny, v)
                point[k] = v
    if flag or maxx < 0 or minx > 1 or maxy < 0 or miny > 1:
       print("raise AssertionError('Frame bounds are not coming proper')")   
    new_width = maxx - minx
    new_length = maxy - miny
    return minx, miny, new_width, new_length


def update_mask(mask_points, frame):
    x, y, h, w = frame['x'], frame['y'], frame['h'], frame['w']
    for point in mask_points:
        for k,_ in point.items():
            if k.endswith('x'):
                point[k] = (point[k] - x) / w
                if point[k] < 0 or point[k] > 1:
                    raise AssertionError('Mask bounds relative to frame are not coming proper')    
            elif k.endswith('y'):
                point[k] = (point[k] - y) / h
                if point[k] < 0 or point[k] > 1:
                    raise AssertionError('Mask bounds relative to frame are not coming proper')    
    return

#your path_to_psx_ios eg. '/Users/khimansh/bug_fix/psx-ios'
path_to_psx_ios = '/Users/garimsin/Documents/psx-ios' 

if path_to_psx_ios == '':
    sys.exit('Please give your psx-ios path in the code at line 43')
    

#theme's name to change
new_themes = [
                "LayoutBBQ_GR_002"
            ]

print(*new_themes, sep = "\n")
print("These theme's layout files are going to change, you can change this list in the code")


files_path = f"{path_to_psx_ios}/PSExpress/Classes/Collage/ThemeAssets/LayoutDescriptions"
cnt = 0
for theme in new_themes:
    #files = layout files of {theme}
    files = os.listdir(f'{files_path}/{theme}')
    for fl in files:
        #taking only files in the format of "Layout(.*?).json"
        if fl.startswith('.') or not fl.startswith('Layout') or not fl.endswith('.json'):
            continue
        print(fl)
        json_data = open(f'{files_path}/{theme}/{fl}', 'r').read()
        parsed_json = (json.loads(json_data))
        if 'CollageStateGCells' in parsed_json:
            #cells = no_of_cells in layout
            cells = parsed_json['CollageStateGCells']
            for cell in cells:
                frame = cell['CellStateNCFrame']
                if 'CellStateCellMask' in cell:
                    frame['x'], frame['y'] , frame['w'], frame['h'] = bound(cell['CellStateCellMask'], frame)
                    update_mask(cell['CellStateCellMask'], frame)
                else:
                    print(f'CellStateCellMask key in not present in {theme}/{fl} file, It is not an error, but check the file once')
            cnt += 1
            open(f'{files_path}/{theme}/{fl}', 'w').write(json.dumps(parsed_json, indent=4, sort_keys=True))
        else:
            print(f'{theme}/{fl} is not proper json file describing a layout, check it once as CollageStateGCells key not present in this json file')
print(f'{cnt} no of files changed, Thanks :)')
import materials

def read_file_data(filename:str) -> list[materials.Material]:
    mats = []
    try:
        with open(filename) as file_object:
            for line in file_object:
                info = line.split(',')
                mats.append(materials.Material(info[0],float(info[1])))
    except Exception as e:
        print(f"{e} was thrown but handled.")
    return mats

def override_file_data(filename:str,materials:list[materials.Material]) -> bool:
    success = True
    try:
        with open(filename,"w") as file_object:
            for material in materials:
                file_object.write(material.file_format())
    except Exception as e:
        success = False
        print(f"{e} was thrown but handled.")
    return success

def update_file_data(filename:str,materials:list[materials.Material]):
    try:
        with open(filename,"a") as file_object:
            for material in materials:
                file_object.write(material.file_format())
    except Exception as e:
        success = False
        print(f"{e} was thrown but handled.")

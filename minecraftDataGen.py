import json
import os

#potentially change texture name for stais, slabs, fences, etc.
#eg.: "texture": "baobab" -> "texture": "baobab_planks"

#change double slab model in slab blockstate files
#eg.: "model": "limestone_slab" -> "model": "limestone"

#---<names in genData.json>---
#"block": "NAME"
#"stairs": "NAME_stairs"
#"slab": "NAME_slab"
#"button": "NAME_button"
#"door": "NAME_door"
#"pressure_plate": "NAME_pressure_plate"
#"fence": "NAME_fence"
#"fence_gate": "NAME_fence_gate"
#"pillar_block": "NAME"
#"sign": "NAME_sign"
#"trapdoor": "NAME_trapdoor"
#"wall": "NAME_wall"

def createDirectories():
    if not os.path.exists(getFilePath('output/blockstates')):
        os.makedirs(getFilePath('output/blockstates'))
    if not os.path.exists(getFilePath('output/loot_tables/blocks')):
        os.makedirs(getFilePath('output/loot_tables/blocks'))
    if not os.path.exists(getFilePath('output/models/block')):
        os.makedirs(getFilePath('output/models/block'))
    if not os.path.exists(getFilePath('output/models/item')):
        os.makedirs(getFilePath('output/models/item'))

def getFilePath(file_dir):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, file_dir)

def readFile(path):
    with open(getFilePath(path), "r") as read_file:
        data = json.dumps(json.load(read_file))
        return data

def writeFile(path, data):
    with open(getFilePath(path), "w") as write_file:
        json.dump(json.loads(data), write_file, indent=4)

def replaceData(mod_id, name, data):
    data = data.replace("MODID", mod_id)
    data = data.replace("NAME", name)
    return data

def createBlockAssets(mod_id, name):
    #model
    data = readFile("templates/models/block/blockTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + ".json"), data)
    #item model
    data = readFile("templates/models/item/blockItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/blockTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createStairAssets(mod_id, name):
    truncated_name = name.replace("_stairs", '')
    #model
    data = readFile("templates/models/block/stairsTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + ".json"), data)
    #inner model
    data = readFile("templates/models/block/stairsInnerTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_inner.json"), data)
    #outer model
    data = readFile("templates/models/block/stairsOuterTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_outer.json"), data)
    #item model
    data = readFile("templates/models/item/blockItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/stairsTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createSlabAssets(mod_id, name):
    truncated_name = name.replace("_slab", '')
    #slab model
    data = readFile("templates/models/block/slabTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + ".json"), data)
    #slab top model
    data = readFile("templates/models/block/slabTopTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_top.json"), data)
    #item model
    data = readFile("templates/models/item/blockItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/slabTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSlabTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createButtonAssets(mod_id, name):
    truncated_name = name.replace("_button", '')
    #pressed model
    data = readFile("templates/models/block/buttonPressedTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_pressed.json"), data)
    #button model
    data = readFile("templates/models/block/buttonTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + ".json"), data)
    #inventory model
    data = readFile("templates/models/block/buttonInventoryTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_inventory.json"), data)
    #item model
    data = readFile("templates/models/item/inventoryItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/buttonTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createDoorAssets(mod_id, name):
    #bottom model
    data = readFile("templates/models/block/doorBottomTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + "_bottom.json"), data)
    #bottom hinge model
    data = readFile("templates/models/block/doorBottomHingeTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + "_bottom_hinge.json"), data)
    #top model
    data = readFile("templates/models/block/doorTopTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + "_top.json"), data)
    #top hinge model
    data = readFile("templates/models/block/doorTopHingeTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + "_top_hinge.json"), data)
    #item model
    data = readFile("templates/models/item/itemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/doorTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropDoorTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createPressurePlateAssets(mod_id, name):
    truncated_name = name.replace("_pressure_plate", '')
    #pressure plate model
    data = readFile("templates/models/block/pressurePlateTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + ".json"), data)
    #pressure plate down model
    data = readFile("templates/models/block/pressurePlateDownTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_down.json"), data)
    #item model
    data = readFile("templates/models/item/blockItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/pressurePlateTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createFenceAssets(mod_id, name):
    truncated_name = name.replace("_fence", '')
    #fence side model
    data = readFile("templates/models/block/fenceSideTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_side.json"), data)
    #fence post model
    data = readFile("templates/models/block/fencePostTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_post.json"), data)
    #inventory model
    data = readFile("templates/models/block/fenceInventoryTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_inventory.json"), data)
    #item model
    data = readFile("templates/models/item/inventoryItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/fenceTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createFenceGateAssets(mod_id, name):
    truncated_name = name.replace("_fence_gate", '')
    #fence gate model
    data = readFile("templates/models/block/fenceGateTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + ".json"), data)
    #fence gate open model
    data = readFile("templates/models/block/fenceGateOpenTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_open.json"), data)
    #fence gate wall model
    data = readFile("templates/models/block/fenceGateWallTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_wall.json"), data)
    #fence gate wall open model
    data = readFile("templates/models/block/fenceGateWallOpenTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_wall_open.json"), data)
    #item model
    data = readFile("templates/models/item/blockItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/fenceGateTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createOrientablePillarBlockAssets(mod_id, name):
    #model
    data = readFile("templates/models/block/pillarBlockTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + ".json"), data)
    #item model
    data = readFile("templates/models/item/blockItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/pillarBlockTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)
    
def createPillarBlockAssets(mod_id, name):
    #model
    data = readFile("templates/models/block/pillarBlockTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + ".json"), data)
    #item model
    data = readFile("templates/models/item/blockItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/blockTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createSignAssets(mod_id, name):
    truncated_name = name.replace("_sign", '')
    #sign model
    data = readFile("templates/models/block/signTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + ".json"), data)
    #item model
    data = readFile("templates/models/item/itemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/signTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #wall blockstate
    data = readFile("templates/blockstates/wallSignTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + truncated_name + "_wall_sign.json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createTrapdoorAssets(mod_id, name):
    #trapdoor bottom model
    data = readFile("templates/models/block/trapdoorBottomTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + "_bottom.json"), data)
    #trapdoor top model
    data = readFile("templates/models/block/trapdoorTopTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + "_top.json"), data)
    #trapdoor open model
    data = readFile("templates/models/block/trapdoorOpenTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + "_open.json"), data)
    #item model
    data = readFile("templates/models/item/trapdoorItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/trapdoorTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createWallAssets(mod_id, name):
    truncated_name = name.replace("_wall", '')
    #wall side model
    data = readFile("templates/models/block/wallSideTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_side.json"), data)
    #wall side tall model
    data = readFile("templates/models/block/wallSideTallTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_side_tall.json"), data)
    #wall post model
    data = readFile("templates/models/block/wallPostTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_post.json"), data)
    #inventory model
    data = readFile("templates/models/block/wallInventoryTemplate.json")
    data = replaceData(mod_id, truncated_name, data)
    writeFile(("output/models/block/" + name + "_inventory.json"), data)
    #item model
    data = readFile("templates/models/item/inventoryItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/wallTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)
    
def createPlantAssets(mod_id, name):
    #model
    data = readFile("templates/models/block/plantTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + ".json"), data)
    #item model
    data = readFile("templates/models/item/plantItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/plantTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropSelfTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createTallPlantAssets(mod_id, name):
    #model bottom
    data = readFile("templates/models/block/tallPlantBottomTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + "_bottom.json"), data)
    #model top
    data = readFile("templates/models/block/tallPlantTopTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/block/" + name + "_top.json"), data)
    #item model
    data = readFile("templates/models/item/tallPlantItemTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/models/item/" + name + ".json"), data)
    #blockstate
    data = readFile("templates/blockstates/tallPlantTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/blockstates/" + name + ".json"), data)
    #loot_table
    data = readFile("templates/loot_tables/blocks/dropTallPlantTemplate.json")
    data = replaceData(mod_id, name, data)
    writeFile(("output/loot_tables/blocks/" + name + ".json"), data)

def createAssets():
    data = json.loads(readFile("genData.json"))
    mod_id = data["mod_id"]
    for name in data["block"]:
        createBlockAssets(mod_id, name)
    for name in data["stairs"]:
        createStairAssets(mod_id, name)
    for name in data["slab"]:
        createSlabAssets(mod_id, name)
    for name in data["button"]:
        createButtonAssets(mod_id, name)
    for name in data["door"]:
        createDoorAssets(mod_id, name)
    for name in data["pressure_plate"]:
        createPressurePlateAssets(mod_id, name)
    for name in data["fence"]:
        createFenceAssets(mod_id, name)
    for name in data["fence_gate"]:
        createFenceGateAssets(mod_id, name)
    for name in data["orientable_pillar_block"]:
        createOrientablePillarBlockAssets(mod_id, name)
    for name in data["pillar_block"]:
        createPillarBlockAssets(mod_id, name)
    for name in data["sign"]:
        createSignAssets(mod_id, name)
    for name in data["trapdoor"]:
        createTrapdoorAssets(mod_id, name)
    for name in data["wall"]:
        createWallAssets(mod_id, name)
    for name in data["plant"]:
        createPlantAssets(mod_id, name)
    for name in data["tall_plant"]:
        createTallPlantAssets(mod_id, name)

createDirectories()
createAssets()
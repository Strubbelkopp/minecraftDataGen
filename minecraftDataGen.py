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

def saveNewFile(mod_id, replace_name, template_path, output_path):
    data = readFile(template_path)
    data = replaceData(mod_id, replace_name, data)
    writeFile((output_path), data)

def createBlockAssets(mod_id, name):
    #model
    saveNewFile(mod_id, name, "templates/models/block/blockTemplate.json", "output/models/block/" + name + ".json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/blockItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/blockTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createStairAssets(mod_id, name):
    truncated_name = name.replace("_stairs", '')
    if("brick" in truncated_name):
        truncated_name = truncated_name.replace("brick", "bricks")
    #model
    saveNewFile(mod_id, truncated_name, "templates/models/block/stairsTemplate.json", "output/models/block/" + name + ".json")
    #inner model
    saveNewFile(mod_id, truncated_name, "templates/models/block/stairsInnerTemplate.json", "output/models/block/" + name + "_inner.json")
    #outer model
    saveNewFile(mod_id, truncated_name, "templates/models/block/stairsOuterTemplate.json", "output/models/block/" + name + "_outer.json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/blockItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/stairsTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createSlabAssets(mod_id, name):
    truncated_name = name.replace("_slab", '')
    if("brick" in truncated_name):
        truncated_name = truncated_name.replace("brick", "bricks")
    #slab model
    saveNewFile(mod_id, truncated_name, "templates/models/block/slabTemplate.json", "output/models/block/" + name + ".json")
    #slab top model
    saveNewFile(mod_id, truncated_name, "templates/models/block/slabTopTemplate.json", "output/models/block/" + name + "_top.json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/blockItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, truncated_name, "templates/blockstates/slabTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSlabTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createButtonAssets(mod_id, name):
    truncated_name = name.replace("_button", '')
    if("brick" in truncated_name):
        truncated_name = truncated_name.replace("brick", "bricks")
    #pressed model
    saveNewFile(mod_id, truncated_name, "templates/models/block/buttonPressedTemplate.json", "output/models/block/" + name + "_pressed.json")
    #button model
    saveNewFile(mod_id, truncated_name, "templates/models/block/buttonTemplate.json", "output/models/block/" + name + ".json")
    #inventory model
    saveNewFile(mod_id, truncated_name, "templates/models/block/buttonInventoryTemplate.json", "output/models/block/" + name + "_inventory.json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/inventoryItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/buttonTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createDoorAssets(mod_id, name):
    #bottom model
    saveNewFile(mod_id, name, "templates/models/block/doorBottomTemplate.json", "output/models/block/" + name + "_bottom.json")
    #bottom hinge model
    saveNewFile(mod_id, name, "templates/models/block/doorBottomHingeTemplate.json", "output/models/block/" + name + "_bottom_hinge.json")
    #top model
    saveNewFile(mod_id, name, "templates/models/block/doorTopTemplate.json", "output/models/block/" + name + "_top.json")
    #top hinge model
    saveNewFile(mod_id, name, "templates/models/block/doorTopHingeTemplate.json", "output/models/block/" + name + "_top_hinge.json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/itemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/doorTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropDoorTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createPressurePlateAssets(mod_id, name):
    truncated_name = name.replace("_pressure_plate", '')
    if("brick" in truncated_name):
        truncated_name = truncated_name.replace("brick", "bricks")
    #pressure plate model
    saveNewFile(mod_id, truncated_name, "templates/models/block/pressurePlateTemplate.json", "output/models/block/" + name + ".json")
    #pressure plate down model
    saveNewFile(mod_id, truncated_name, "templates/models/block/pressurePlateDownTemplate.json", "output/models/block/" + name + "_down.json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/blockItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/pressurePlateTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createFenceAssets(mod_id, name):
    truncated_name = name.replace("_fence", '')
    if("brick" in truncated_name):
        truncated_name = truncated_name.replace("brick", "bricks")
    #fence side model
    saveNewFile(mod_id, truncated_name, "templates/models/block/fenceSideTemplate.json", "output/models/block/" + name + "_side.json")
    #fence post model
    saveNewFile(mod_id, truncated_name, "templates/models/block/fencePostTemplate.json", "output/models/block/" + name + "_post.json")
    #inventory model
    saveNewFile(mod_id, truncated_name, "templates/models/block/fenceInventoryTemplate.json", "output/models/block/" + name + "_inventory.json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/inventoryItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/fenceTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createFenceGateAssets(mod_id, name):
    truncated_name = name.replace("_fence_gate", '')
    if("brick" in truncated_name):
        truncated_name = truncated_name.replace("brick", "bricks")
    #fence gate model
    saveNewFile(mod_id, truncated_name, "templates/models/block/fenceGateTemplate.json", "output/models/block/" + name + ".json")
    #fence gate open model
    saveNewFile(mod_id, truncated_name, "templates/models/block/fenceGateOpenTemplate.json", "output/models/block/" + name + "_open.json")
    #fence gate wall model
    saveNewFile(mod_id, truncated_name, "templates/models/block/fenceGateWallTemplate.json", "output/models/block/" + name + "_wall.json")
    #fence gate wall open model
    saveNewFile(mod_id, truncated_name, "templates/models/block/fenceGateWallOpenTemplate.json", "output/models/block/" + name + "_wall_open.json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/blockItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/fenceGateTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createOrientablePillarBlockAssets(mod_id, name):
    #model
    saveNewFile(mod_id, name, "templates/models/block/pillarBlockTemplate.json", "output/models/block/" + name + ".json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/blockItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/pillarBlockTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")
    
def createPillarBlockAssets(mod_id, name):
    #model
    saveNewFile(mod_id, name, "templates/models/block/pillarBlockTemplate.json", "output/models/block/" + name + ".json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/blockItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/blockTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createSignAssets(mod_id, name):
    truncated_name = name.replace("_sign", '')
    if("brick" in truncated_name):
        truncated_name = truncated_name.replace("brick", "bricks")
    #sign model
    saveNewFile(mod_id, truncated_name, "templates/models/block/signTemplate.json", "output/models/block/" + name + ".json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/itemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/signTemplate.json", "output/blockstates/" + name + ".json")
    #wall blockstate
    saveNewFile(mod_id, name, "templates/blockstates/wallSignTemplate.json", "output/blockstates/" + truncated_name + "_wall_sign.json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createTrapdoorAssets(mod_id, name):
    #trapdoor bottom model
    saveNewFile(mod_id, name, "templates/models/block/trapdoorBottomTemplate.json", "output/models/block/" + name + "_bottom.json")
    #trapdoor top model
    saveNewFile(mod_id, name, "templates/models/block/trapdoorTopTemplate.json", "output/models/block/" + name + "_top.json")
    #trapdoor open model
    saveNewFile(mod_id, name, "templates/models/block/trapdoorOpenTemplate.json", "output/models/block/" + name + "_open.json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/trapdoorItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/trapdoorTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createWallAssets(mod_id, name):
    truncated_name = name.replace("_wall", '')
    if("brick" in truncated_name):
        truncated_name = truncated_name.replace("brick", "bricks")
    #wall side model
    saveNewFile(mod_id, truncated_name, "templates/models/block/wallSideTemplate.json", "output/models/block/" + name + "_side.json")
    #wall side tall model
    saveNewFile(mod_id, truncated_name, "templates/models/block/wallSideTallTemplate.json", "output/models/block/" + name + "_side_tall.json")
    #wall post model
    saveNewFile(mod_id, truncated_name, "templates/models/block/wallPostTemplate.json", "output/models/block/" + name + "_post.json")
    #inventory model
    saveNewFile(mod_id, truncated_name, "templates/models/block/wallInventoryTemplate.json", "output/models/block/" + name + "_inventory.json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/inventoryItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/wallTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")
    
def createPlantAssets(mod_id, name):
    #model
    saveNewFile(mod_id, name, "templates/models/block/plantTemplate.json", "output/models/block/" + name + ".json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/plantItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/plantTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropSelfTemplate.json", "output/loot_tables/blocks/" + name + ".json")

def createTallPlantAssets(mod_id, name):
    #model bottom
    saveNewFile(mod_id, name, "templates/models/block/tallPlantBottomTemplate.json", "output/models/block/" + name + "_bottom.json")
    #model top
    saveNewFile(mod_id, name, "templates/models/block/tallPlantTopTemplate.json", "output/models/block/" + name + "_top.json")
    #item model
    saveNewFile(mod_id, name, "templates/models/item/tallPlantItemTemplate.json", "output/models/item/" + name + ".json")
    #blockstate
    saveNewFile(mod_id, name, "templates/blockstates/tallPlantTemplate.json", "output/blockstates/" + name + ".json")
    #loot_table
    saveNewFile(mod_id, name, "templates/loot_tables/blocks/dropTallPlantTemplate.json", "output/loot_tables/blocks/" + name + ".json")

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
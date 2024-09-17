from fastapi import APIRouter
from models.presidents import President
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from utils.prompts import select_prompts, prompts

router = APIRouter()

#GET Request Method
@router.get("/")
async def get_presidents():
    presidents = list_serial(collection_name.find())
    return presidents

#GET Request Method for Prompts
@router.get("/select_prompts")
async def get_selected_prompts():
    selected_prompts = select_prompts(prompts, collection_name)
    return {
        "top_prompts": selected_prompts["top_prompts"],
        "side_prompts": selected_prompts["side_prompts"],
        "matched_presidents": selected_prompts["matched_presidents"]
    }


#POST Request Method
@router.post("/")
async def post_president(president: President):
    collection_name.insert_one(dict(president))

#PUT Request Method
@router.put("/{id}")
async def put_president(id: str, president: President):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(president)})

#DELETE Request Method
@router.delete("/{id}")
async def delete_president(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})

#GET Names Method
@router.get("/getnames")
async def get_names():
    presidents = list_serial(collection_name.find({}, {"name": 1, "_id": 0}), name_only=True)
    return presidents


#add method for intializing game
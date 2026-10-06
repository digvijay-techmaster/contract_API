from fastapi.responses import JSONResponse
from fastapi import Request


class PincodeNotFoundError(Exception):
    def __init__(self, pincode:str):
        self.pincode=pincode
    '''__init__ is a special Python function.
It runs automatically when you create an object from the class.
Take the current object and herre self represent the current object 
        ↓
give it an attribute called "pincode"
        ↓
put the value of "pincode" into it'''
class InvalidPinCodeError(Exception):
    def __init__(self,pincode:str,reason:str="Invalid format"):
        self.pincode=pincode
        self.reason=reason

#cusom excetion handellers
async def pincode_not_found_handeler(request:Request,exc:PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"pincode_not_found",
            "message":f"np location for pincode :{exc.pincode}",
            "pincode":exc.pincode
        }
    )
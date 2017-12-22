
from .wrapper import Wrapper 
from flask import Response
import traceback
import json
import logging
 
class ResponseBody( Wrapper ):

    def __to_result( self, success, result, error = None):
        default_params = self.get_default_params()
        kwargs = default_params.get("kwargs")
        response_type = kwargs.get("response_type")
        data = dict()

        if success:
            data["result"] = result
        else:
            data["errorMsg"] = error
        data["success"] = success

        return data

    def wrap( self, fn, input_params ):
 
        try:
            results = fn()
            resp_result = []
            pageable = None

            resp_result = results
 
            data = self.__to_result(True, resp_result)
        except Exception as e:
            data = self.__to_result( False, None, str(e) )
            logging.error(traceback.format_exc())
 
        return Response( json.dumps( data ) , mimetype="application/json" )


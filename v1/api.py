import requests
import json

class Validador:

    # Function to convert HTML result into json Object
    def ConvertirAJson(result, curp):    
        # Temporal Key for next iteration
        key = ""
        assignValue = False
        data = {}

        for line in result.iter_lines():

            # Convert from byte to ASCII 
            line = line.decode("ASCII")

            # If line includes this div, the line should include key and value
            if 'div align="left"' in line:

                # check if the iteration is for value assignation
                if assignValue:
                    # Value must be added to json with temporal key
                    data[key] = line[line.index('left">')+6 : line.index('</div')]
                    assignValue = False
                    continue

                if assignValue is False:
                    # Insert Key and replace :
                    key = line[line.index('left">')+6 : line.index('</div') - 1]
                    assignValue = True
            
            elif 'TipoError' in line:
                data['Error'] = "El formato de CURP o datos generales son incorrectos."
                data['msg'] = curp
            
        
        # Data dump into json object
        json_curp = json.dumps(data, indent=4, sort_keys=True)
        return json_curp

    def CURP(curp):
        # URL endpoint => http://www.renapo.sep.gob.mx/wsrenapo/MainControllerParam
        # Using POST
        url = "http://www.renapo.sep.gob.mx/wsrenapo/MainControllerParam"
        
        # set curp as param
        #param = curp --> the parameter should be included before call the post function
        param = "curp=" + curp

        # convert Request to json
        result = requests.post(url = url, params = param)

        return Validador.ConvertirAJson(result, curp)
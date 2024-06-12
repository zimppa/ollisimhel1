from flask import Flask, request
from timemana_service import db_add_hours, db_get_hours

app = Flask(__name__)

#region POST
@app.route("/time_management", methods=['POST'])
def add_hours():
    try: 
        data = request.get_json()
        startTime = data['startTime']
        endTime = data['endTime']
        lunchBreak = data['lunchBreak']
        consultantName = data['consultantName']
        customerName = data['customerName']
        
        db_add_hours(startTime, endTime, lunchBreak, consultantName, customerName)
        return {"success": "Added hours logged by: %s" % consultantName}
    except:
        return {"error": "error adding hours"}
#endregion POST



# testikäyttöön GET funktio. Todellisuudessa Azuressa on valmiina taulu johon vain insertataan dataa.
#region GET
@app.route("/", methods=["GET"])
def index():
    return {"index": True}

@app.route('/time_management', methods=['GET'])
def get_all_hours():
    try:  
        return db_get_hours()
    except:
        return {"error": "no data"}
#endregion GET

if __name__ == "__main__":
    app.run()
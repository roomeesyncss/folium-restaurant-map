from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():

    map_var = folium.Map(location=[24.8607, 67.0011])  # Karachi's approximate center

    restaurants = [
        {"name": "Restaurant A", "location": [24.9349, 67.0635]},
        {"name": "Restaurant B", "location": [24.9522, 67.0803]},
        {"name": "Restaurant C", "location": [24.9418, 67.0777]},
        {'name': 'Restaurant D' , 'location': [24.936183525118786, 67.09949589042728]}
        # Add more restaurants here
    ]


    for restaurant in restaurants:
        name = restaurant["name"]
        location = restaurant["location"]
        folium.Marker(location=location, popup=name).add_to(map_var)


    map_html = map_var.get_root().render()

    return render_template('index.html', map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)

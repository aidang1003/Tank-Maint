from flask import Flask
from flask import render_template, request, redirect


app = Flask(__name__)



class Tank():
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
    def __str__(self):
        return "Tank with radius {} ft and height {} ft, will cost ${} total".format(self.radius, self.height, self.totalCost())
        
    def tankTopArea(self):
        return 3.14 * (self.radius ** 2)
    
    def tankSideArea(self):
        return (2 * (3.14 * self.radius)) * self.height
    
    def tankTotalArea(self):
        return self.tankSideArea() + self.tankTopArea()
    
    def materialCost(self):
        return round(self.tankTotalArea() * 25, 2)
    
    def laborCost(self):
        return round(self.tankTotalArea() * 15, 2)
    
    def totalCost(self):
        return '${0:.2f}'.format(self.materialCost() + self.laborCost())

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Homepage')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate', methods=["GET","POST"])
def estimate():
    
    if request.method == "POST":
        form = request.form

        tRadius = float(form['tRadius'])
        tHeight = float(form['tHeight'])

        tank = Tank(tRadius, tHeight)
        
        tankCost = tank.totalCost()

        return render_template('estimate.html', tankCost=tankCost)

    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, jsonify

app = Flask(__name__)

class MapColoringCSP:
    def __init__(self, variables, colors, neighbors):
        self.variables = variables
        self.colors = colors
        self.neighbors = neighbors
        self.steps = []  # Lưu lại lịch sử các bước để tạo animation trên web
#Bao GIa
    def is_valid(self, variable, color, assignment):
        for neighbor in self.neighbors.get(variable, []):
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def select_unassigned_variable(self, assignment):
        unassigned = [v for v in self.variables if v not in assignment]
        # Heuristic: Chọn vùng có nhiều hàng xóm nhất
        unassigned.sort(key=lambda var: len(self.neighbors.get(var, [])), reverse=True)
        return unassigned[0]

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return True

        var = self.select_unassigned_variable(assignment)

        for color in self.colors:
            self.steps.append({"region": var, "color": color, "type": "try", "msg": f"Thử {var} = {color}"})
            
            if self.is_valid(var, color, assignment):
                assignment[var] = color
                self.steps.append({"region": var, "color": color, "type": "assign", "msg": f"Hợp lệ: Gán {var} = {color}"})
                
                if self.backtrack(assignment):
                    return True
                
                # Nếu sai thì quay lui
                self.steps.append({"region": var, "color": "white", "type": "backtrack", "msg": f"Quay lui {var}"})
                del assignment[var]
            else:
                self.steps.append({"region": var, "color": "white", "type": "invalid", "msg": f"Sai: {var} không thể là {color}"})
                
        return False

    def solve(self):
        self.steps = []
        self.backtrack({})
        return self.steps

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve')
def solve_map():
    regions = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    # Dùng tiếng Anh để file JS gán trực tiếp vào CSS fill
    colors = ["red", "green", "blue"] 
    neighbors = {
"A": ["B", "C"],
        "B": ["A", "C", "D", "E"],
        "C": ["A", "B", "E", "F"],
        "D": ["B", "E", "G"],
        "E": ["B", "C", "D", "F", "G", "H"], 
        "F": ["C", "E", "H"],
        "G": ["D", "E", "H"],               
        "H": ["E", "F", "G", "J"],
        "I": ["J"],
        "J": ["H", "I"]
}

    csp = MapColoringCSP(regions, colors, neighbors)
    steps = csp.solve()
    
    return jsonify({"success": True, "steps": steps})

if __name__ == '__main__':
    app.run(debug=True)
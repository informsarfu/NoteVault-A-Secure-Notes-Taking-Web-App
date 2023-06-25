from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
# <ul class="list-group list-group-flush" id="notes">  
# <li class="list-group-item">
#     {{ note.text }}
#   </li>
#   {% endfor %}
# </ul>

    
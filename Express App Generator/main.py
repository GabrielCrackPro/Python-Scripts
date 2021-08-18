import os

def run(cmd):
    print(cmd)
    os.system(cmd)
def write(file,content):
    f = open(file,"w+")
    f.write(content)
    f.write("\n")

index_content = """
const express = require("express")
const cors = require("cors")
const morgan = require("morgan")

const public = express.static("public")

const app = express()
const port = process.env.PORT || 3000

app.use(cors())
app.use(morgan("dev"))
app.use(public)

app.listen(port, () => {
console.log(`Listening on port ${port}...`)
})
"""
html_content = """
<!DOCTYPE html>
<html lang=en>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
</head>
<body>

</body>
</html>
"""

commands = [
        "npm init -y",
        "npm --silent express cors morgan",
        "npm i --silent nodemon --save-dev",
        "touch index.js",
        "mkdir public",
        "cd public",
        "touch index.html && touch style.css && touch app.js",
        "cd .."
        ]
for range(len(comands)) in comands :
    run(comand)
print("Express app create successfully")

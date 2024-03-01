function getNumberOfOptions(){
    return 0;
}

async function getQuestion(){

    const response = await fetch("/api", 
    {
        method: "GET",
        args: {type: "question"}
    });
    const result = await response.json();
    alert("here");

    response.then((data)=>{
        alert(data);
    });
    return "im a question"
}

function listOfOptions(){
    return [
        "option 1 example",
        "option 2 example",
        "option 3 example",
        "option 4 example",
    ]
}


getQuestion();
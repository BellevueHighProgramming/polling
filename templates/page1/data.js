function getNumberOfOptions(){
    return 0;
}

function getQuestion(){
    new Request("/api", {
        method: "GET",
        body: '{"type": "question"}',
    }).then((response) => {
        if (response.status === 200) {
          return response.json();
        } else {
          throw new Error("Something went wrong on API server!");
        }
    })

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


alert(getQuestion());
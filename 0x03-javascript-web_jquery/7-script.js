$.getJSON("https://swapi-api.hbtn.io/api/people/5/?format=json", function({name}) {
  $("#character").text(name);
});
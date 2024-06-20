const express = require("express");
const { join } = require("path");
const app = express();

app.use(express.static(join(__dirname, "./public")));

app.get("/", (req, res) => {
	res.send("public/index.html");
});

app.listen((3000), () => {
	console.log(`site is up`);
});

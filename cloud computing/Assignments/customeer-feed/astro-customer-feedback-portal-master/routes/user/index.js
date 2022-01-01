var express = require('express');
var router = express.Router();

const User = require('../../services/user');

router.get("/get-all", (req, res, next) => {
    try {
        User.getAll().then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

module.exports = router;

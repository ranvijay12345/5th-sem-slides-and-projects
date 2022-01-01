var express = require('express');
var router = express.Router();

const Review = require('../../services/review');

router.get("/get-all", (req, res, next) => {
    try {
        Review.getAll().then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.post("/add-new", (req, res, next) => {
    try {
        Review.addNew({
            data: req.body
        }).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.post("/update-rating", (req, res, next) => {
    try {
        Review.updateRating({
            data: req.body
        }).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.get("/get-review-types", (req, res, next) => {
    try {
        Review.getReviewTypes().then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.get("/get-review-by-email/:email", (req, res, next) => {
    try {
        Review.getReviewByEmail(req.params.email).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

module.exports = router;

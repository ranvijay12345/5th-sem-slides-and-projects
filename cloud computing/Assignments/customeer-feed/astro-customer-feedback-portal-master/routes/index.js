var express = require('express')
var router = express.Router()

const UserFileRouter = require('./user')
const ReviewFileRouter = require('./review/')
const DashboardFileRouter = require('./dashboard/')
const CaseDetailFileRouter = require('./case-detail/')

router.use('/user', UserFileRouter)
router.use('/review', ReviewFileRouter)

router.use('/dashboard', DashboardFileRouter)
router.use('/case-detail', CaseDetailFileRouter)

module.exports = router

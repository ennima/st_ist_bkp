var express = require('express');
var router = express.Router();
var Slack = require('slack-node');
 
webhookUri = "https://hooks.slack.com/services/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";
slack = new Slack();
slack.setWebhook(webhookUri);

slack.webhook({
  channel: "#general",
  username: "webhookbot",
  text: "This is posted to #general and comes from a bot named webhookbot."
}, function(err, response) {
  console.log(response);
});


/* GET home page. */
router.get('/', function(req, res, next) {
	slack.webhook({
	  channel: "#aleatorio",
	  username: "webhooker",
	  icon_emoji: "http://icons.iconarchive.com/icons/rokey/popo-emotions/128/after-boom-icon.png",
	  text: "test message, test message"
	}, function(err, response) {
	  console.log(response);
	});
  res.render('index', { title: 'Express' });
});

module.exports = router;

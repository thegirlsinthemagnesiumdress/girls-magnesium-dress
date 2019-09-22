const Google = require('googleapis');
const cors = require('cors');
const BUCKET = 'annaastesano.appspot.com'; // Replace with name of your bucket

const API_KEY = '335cce738241a01d6ab9765dfa839ca7';
const API_SECRET = '9a89ae753ad8a7c731904e23d49c4129';
const mailjet = require ('node-mailjet').connect(API_KEY, API_SECRET);

var corsFn = cors({origin: true});

function getAccessToken(header) {
    if (header) {
        var match = header.match(/^Bearer\s+([^\s]+)$/);
        if (match) {
            return match[1];
        }
    }

    return null;
}


function authorized(res) {
    res.send("The request was successfully authorized.");
}




const mailJetSend = () => {

  const request = mailjet
    .post("send")
    .request({
        "FromEmail":"killer.paolo@gmail.com",
        "FromName":"Anaa Astesano",
        "Subject":"Test email",
        "Text-part":"Dear passenger, welcome to Mailjet! May the delivery force be with you!",
        "Html-part":"<h3>Dear passenger, welcome to Mailjet!</h3><br />May the delivery force be with you!",
        "Recipients":[{"Email":"killer.paolo@gmail.com"}]
    });
    return request
      .then(result => {
          console.log(result.body)
      	return result.body;
      })
      .catch(err => {
          console.log(err.statusCode)
	      return err;
      })
}



/**
 * Cloud Function.
 *
 * @param {Object} req Cloud Function request context.
 * @param {Object} res Cloud Function response context.
 */
const send = function secureFunction(req, res) {
    var accessToken = getAccessToken(req.get('Authorization'));
    var oauth = new Google.auth.OAuth2();

    oauth.setCredentials({access_token: accessToken});

    var permission = 'storage.buckets.get';
    var gcs = Google.storage('v1');
    gcs.buckets.testIamPermissions(
        {bucket: BUCKET, permissions: [permission], auth: oauth}, {},
        function (err, response) {
            if (response && response['permissions'] && response['permissions'].includes(permission)) {
	            mailJetSend().
                	then((data) => {
                   		res.send(data);
                	}, (data) => {
                   		res.send(data);
                	});
            } else {
                res.status(403).send(err);
            }
        });
};

 exports.sendEmail = function(req, res) {
    corsFn(req, res, function() {
        send(req, res);
    });
 };

//exports.sendEmail = send;

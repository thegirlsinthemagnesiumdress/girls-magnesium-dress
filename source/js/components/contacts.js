// var url = 'https://us-central1-annaastesano.cloudfunctions.net/sendEmail';
// const componentSelector = '[data-js-contacts]';
// const token = 'ya29.c.ElnJBU9dE5WOTPzhMeTBfi9a9XwO75quPEM6WB8OvH9bEbGLzyGl7kom9zl4mhjQTlnqUq0bL6AJ4TyxKuvkfUWosJkTw4b2k0V6ar2C0xOUctJcYmV6JgkTuw';
// const data = {
//   "Messages": [
//           {
//       "From": {
//         "Email": "annastesano@gmail.com",
//         "Name": "AnnaAstesano"
//       },
//       "To": [
//           {
//             "Email": "killer.paolo@gmail.com",
//           "Name": "passenger 1"
//         }
//       ],
//       "Subject": "Your email flight plan!",
//       "TextPart": "Dear passenger 1, welcome to Mailjet! May the delivery force be with you!",
//       "HTMLPart": "<h3>Dear passenger 1, welcome to Mailjet!</h3><br/>May the delivery force be with you!"
//     }
//   ]
// };

// let headers = new Headers();
// // const auth = window.btoa(API_KEY + ":" + API_SECRET);

// headers.append('Content-Type', 'application/json');
// headers.append('Authorization', `Bearer ${token}`);

// const sendEmail = () => {
//   fetch(new Request(url), {
//     method: 'POST', // or 'PUT'
//     body: JSON.stringify(data), // data can be `string` or {object}!
//     headers: new Headers({
//       'Authorization': `Bearer ${token}`,
//     }),
//     mode: 'cors',
//   }).then(res => res.json())
//   .catch(error => console.error('Error:', error))
//   .then(response => console.log('Success:', response));
// }

// const init = () => {
//   const contacts = document.querySelector(componentSelector);
//   const form = contacts.querySelector('form');
//   form.addEventListener('submit', (e) =>{
//     sendEmail();
//     e.preventDefault();
//   });
// }


// export {
//   init,
// }

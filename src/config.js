// Initialize Firebase
import Firebase from "firebase";
var config = {
  apiKey: "AIzaSyDmAbxTQVqypx52OxO8mxYHXXisoDD7YW8",
  authDomain: "bt3103careerplanningdata.firebaseapp.com",
  databaseURL: "https://bt3103careerplanningdata.firebaseio.com",
  projectId: "bt3103careerplanningdata",
  storageBucket: "bt3103careerplanningdata.appspot.com",
  messagingSenderId: "895274224140"
};

let app = Firebase.initializeApp(config);
let db = app.database();
let ges = db.ref();

export { ges, db };

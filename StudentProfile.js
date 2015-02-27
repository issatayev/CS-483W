/** 
*	StudentProfile class 
* 	Class for storing profile data of the student
*	Assuming we collected data from LinkedIn basic profile	
*/

function StudentProfile(name, surname, dob, position, location, industry, connections, distance) {
	
	// Default values for the properties
	dob = typeof dob !== 'undefined' ? dob : "None";
	position = typeof position !== 'undefined' ? position : "None";
	location = typeof location !== 'undefined' ? location : "None";
	industry = typeof industry !== 'undefined' ? industry : "None";
	
	this.name = name;
	this.surname = surname;
	this.dob = dob;
	this.position = position;
	this.location = location;
	this.industry = industry;	
	this.connections = {};   	// empty object for connections
	this.distance = {};			// empty object for distance
}

// Method for getting full name of the student
StudentProfile.prototype.fullName = function() {
	console.log(this.name + " " + this.surname);
};

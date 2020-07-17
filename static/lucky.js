/** processForm: get data from form and make AJAX call to our API. */
// Get DOM elements and save them as variables
const $name = $('#name')
const $email = $('#email')
const $year = $('#year')
const $color = $('#color')

async function processForm(evt) {
	evt.preventDefault() //<-- prevents form from reloading page

	// get response from form and save as data object to use in the flask view route
	let apiResp = await axios.post('/api/get-lucky-num', {
		data: {
			name: $name.val(),
			email: $email.val(),
			year: $year.val(),
			color: $color.val(),
		},
	})

	$('#lucky-form').find('input:text').val('') //<-- reset input values after submit
	handleResponse(apiResp) //<-- pass the data into handleResponse
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
	const data = resp.data //<-- save response data as variable
	console.log('DATA:', data)

	// Populate the HTML div with results from API and form data
	$luckyResultDiv = $('#lucky-results')
	$luckyResultDiv.append(
		`<p>Your lucky number is ${data.num.num}. ${data.num.fact}</p>`,
		`<p>Your birth year ${data.year.year}. Fact is ${data.year.fact}</p>`
	)
}

// handle submit
$('#lucky-form').on('submit', processForm)

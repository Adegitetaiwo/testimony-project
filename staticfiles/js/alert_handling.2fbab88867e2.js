$(document).ready(()=>{
    $(document).on('submit', '#subscribe_form', (e) => {
        e.preventDefault();

        let email_input = $('#subscribe_input').val()
        let messageCard = document.getElementById('message-card'),
            message = document.getElementById('message'),
            messageIcon = document.getElementById('message-icon')
        

        const emailIsValid = (mailInput) => {
            return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(mailInput)
        }
            
        $.ajax({
            type: 'POST',
            url: '',
            data: {
                email: email_input,
                csrfmiddlewaretoken: $('input[name= csrfmiddlewaretoken]').val(),
            },

            success: () => {
                if (emailIsValid(email_input)) {
                    //set message card class
                    messageCard.classList.remove('alert-warning')
                    messageCard.classList.add('alert-success')
                    //set success text message
                    message.textContent = 'Thank you for your Subscription, please check your Email for Update'
                    messageIcon.className = 'icon icon-check'

                    //hide form
                    $('#subscribe_form').hide()

                } else {
                    //set message card class
                    messageCard.classList.remove('alert-success')
                    messageCard.classList.add('alert-warning')
                    //set success text message
                    message.textContent = 'Something went wrong please check your email is if it Valid'
                    messageIcon.className = 'icon icon-warning'

                }

            },
            error: () => {
                //set message card class
                messageCard.classList.remove('alert-success')
                messageCard.classList.add('alert-warning')
                //set success text message
                message.textContent = 'Something went wrong please check your email is if it Valid'
                messageIcon.className = 'icon icon-warning'
            },
        })
    });

    $(document).on('submit', '#create_form', (e) => {
        let confirm_form = confirm(`Are you sure you want to submit ? Testimony won't be editable after submission. If you'll still like to cross-check for typo errors Click 'Cancel' otherwise Click 'OK' `);

        if (!confirm_form) {
            e.preventDefault()
        }
    });

});




// $.ajax({
//     type: 'POST',
//     url: '',
//     data: {
//         email: $('#sub_email').val(),
//         csrfmiddlewaretoken: $('input[name= csrfmiddlewaretoken]').val(),
//     },
//     success: () => {
//         let form = document.getElementById('subscribe_form')
//         let mailInput = document.getElementById('sub_email')
//         let MessageDivBox = document.getElementById('message-box')
//         let Message = document.getElementById('message')
//         let MessageIcon = document.getElementById('message-icon')
//         let subscribeCloseDiv = document.getElementById('subscibe-close-btn')


//         //check for valid email
//         const emailIsValid = (mailInput) => {
//             return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(mailInput)
//         }

//         if (emailIsValid(mailInput.value)) {
//             MessageDivBox.className = 'card alert alert-success';
//             Message.textContent = 'Your Subscription was Successful'
//             MessageIcon.className = 'fa fa-check'
//             mailInput.setAttribute('disabled', 'disabled')
//             mailInput.setAttribute('title', 'Disabled')
//             mailInput.setAttribute('style', 'cursor: not-allowed')
//             subscribeCloseDiv.className = 'close'
//         }
//         else {
//             MessageDivBox.className = 'card alert alert-danger';
//             Message.innerText = 'Please enter a valid email'
//             MessageIcon.className = 'fa fa-warning'
//         }

//     },
//     error: () => {
//         MessageDivBox.className = 'card alert alert-danger';
//         Message.innerText = 'Please enter a valid email'
//         MessageIcon.className = 'fa fa-warning'
//     },
// });
            
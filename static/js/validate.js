const ShowPassword = () => {
    let inp = document.getElementById("newPassword")

    if (inp.type == "password") {
        inp.type = "text"
    } else {
        inp.type = "password"
    }
}

const checkValidate = (evt) => {

    let letter = document.getElementById("letter")
    let capital = document.getElementById("capital")
    let number = document.getElementById("number")
    let length = document.getElementById("length")
    let special = document.getElementById("special")

    let isLowerCase = false
    let isUpperCase = false
    let isNumber = false
    let isLength = false
    let isSpecials = false

    let lowerCaseLetters = /[a-z]/g
    let upperCaseLetters = /[A-Z]/g
    let numbers = /[0-9]/g
    // let specialRegex = /[!@#\$%\^\&*\)\(+=._-]/g
    // let specialRegex = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/g
    let specialRegex = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/g

    // Validate lowercase
    if (evt.match(lowerCaseLetters)) {
        letter.classList.remove("invalid")
        letter.classList.add("valid")
        isLowerCase = true
    } else {
        letter.classList.remove("valid")
        letter.classList.add("invalid")
        isLowerCase = false
    }

    // Validate uppercase
    if (evt.match(upperCaseLetters)) {
        capital.classList.remove("invalid")
        capital.classList.add("valid")
        isUpperCase = true
    } else {
        capital.classList.remove("valid")
        capital.classList.add("invalid")
        isUpperCase = false
    }

    // Validate numbers 
    if (evt.match(numbers)) {
        number.classList.remove("invalid")
        number.classList.add("valid")
        isNumber = true
    } else {
        number.classList.remove("valid")
        number.classList.add("invalid")
        isNumber = false
    }

    // Validate special
    if (evt.match(specialRegex)) {
        special.classList.remove("invalid")
        special.classList.add("valid")
        isSpecials = true
    } else {
        special.classList.remove("valid")
        special.classList.add("invalid")
        isSpecials = false
    }


    // Validate length
    if (evt.length >= 8) {
        length.classList.remove("invalid")
        length.classList.add("valid")
        isLength = true
    } else {
        length.classList.remove("valid")
        length.classList.add("invalid")
        isLength = false
    }

    // All true

    submitBTN = document.getElementById("submitBTN")

    isLength && isLowerCase && isUpperCase && isNumber && isSpecials
        ? submitBTN.disabled = false
        : submitBTN.disabled = true
}
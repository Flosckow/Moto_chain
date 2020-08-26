const options = {
    headers: {
        'Authorization': 'JWT ' + localStorage.getItem('auth_key'),
        'Content-Type': 'application/json;charset=utf-8'
    }
}

export default options

const options = {
    headers: {
        'Authorization': 'JWT ' + localStorage.getItem('auth_key'),
        'Content-Type': 'application/json;charset=utf-8'
    }
}
export default options





//export default function fetchAdd(url, params) {
//   // Отправляем запрос
//    fetch(`${url}?${params}`, {
//        method: 'POST',
//        headers: {
//            'Authorization': 'JWT ' + localStorage.getItem('auth_key'),
//            'Content-Type': 'application/json;charset=utf-8'
//        },
//    })
//        .then(response => response.json())
//        .then(json => render(json))
//        .catch(error => console.error(error))
//}
//

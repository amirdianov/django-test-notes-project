export function storeToken(token) {
    localStorage.setItem("token", token);
}

export function getToken() {
    return localStorage.getItem("token");
}

export function clearToken() {
    localStorage.setItem('token', null);
}
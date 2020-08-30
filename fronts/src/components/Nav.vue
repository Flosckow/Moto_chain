<template>
    <div class="main-banner bg bg1" id="home">
        <header class="header">
            <div class="container-fluid px-lg-5">
                <nav class="py-4">
                    <div id="logo">
                        <h1>
                            <a href="#" class="editContent">DjangoShop</a>
                        </h1>
                    </div>
                    <label for="drop" class="toggle">Menu</label>
                    <input type="checkbox" id="drop">
                    <ul class="menu mt-2">
                        <li><button @click="goHome" class="login">Главная</button>
                        <li><button @click="goRegistration" class="login">Регистрация</button>
                        </li>
                        <li><button v-if="!auth" @click="goLogin" class="login">Вход</button>
                        </li>
                        <li><button v-if="auth" @click="goLogout" class="login">Вход</button>
                        </li>
                        <li><button @click="goCart" class="login">Корзина</button>
                        </li>
                    </ul>
                </nav>
            </div>
        </header>
    </div>
</template>

<script>
    export default {
        name: "Nav",
        computed: {
            auth() {
                if (localStorage.getItem('auth_key')) {
                    return true
                }
            },
        },
        methods: {
            goLogin() {
                this.$router.push({name: 'login'})
            },
            goRegistration () {
                this.$router.push({name: 'registration'})
            },
            goHome() {
                this.$router.push({name: 'Home'})
            },
            goLogout() {
                localStorage.removeItem('auth_token')
                window.location = '/'
            },
            goCart() {
                this.$router.push({name: 'Cart'})
            },
        }
    }
</script>

<style scoped>
    #home {
        background-color: rgba(0, 0, 0, 0);
        margin-top: 0;
    }
    .editContent {
        outline: none;
        outline-offset: -2px;
        cursor: inherit;
        color: rgb(0, 0, 0);
        font-size: 40px;
        background-color: rgba(0, 0, 0, 0);
        font-family: Source Sans Pro, sans-serif;
    }
    .login {
        display: inline-block;
        padding: 10px 15px;
        font-size: 14px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        outline: none;
        color: #fff;
        background-color: #dd9475;
        border: none;
        border-radius: 15px;
        box-shadow: 0 9px #999;
        margin-left: 5px;
        margin-right: 5px
    }

    .login:hover {background-color: #bf5830}

    .login:active {
        background-color: #3e8e41;
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }
</style>
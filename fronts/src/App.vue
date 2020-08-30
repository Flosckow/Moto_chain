<template>
    <div id="app">
        <Nav />
        <router-view/>
        <Footer />
    </div>
</template>

<style>
    @import "assets/css/bootstrap.css";
    @import "assets/css/style.css";

</style>
<script>
    import Nav from "./components/Nav";
    import Footer from "./components/Footer"
    import SignIn from "./components/SignIn"
    import SignUp from "./components/SignUp"
    import Cart from "./components/Cart"
    import $ from 'jquery'
    export default {
        name: 'app',
        data () {
            return {
                sign: 'sign-in',
                signComplete: false,
            }
        },
        components: {Nav, Footer, SignIn, SignUp, Cart},
        methods: {
            switchSign(currentSign) {
                this.sign = currentSign;
            }
        }



    }
</script>
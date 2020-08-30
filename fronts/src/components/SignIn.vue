<template>
	<form class="mt-5" @submit.prevent="enterUser">
	    <div class="form group">
			<label for="username">Ваш username:</label>
			<input type ="text" class="form-control" id="username" placeholder="Введите username:" required v-model="user.username">
		</div>
		<div class="form group">
			<label for="email">Ваш email:</label>
			<input type ="email" class="form-control" id="email" placeholder="Введите email:" required v-model="user.email">
		</div>
		<div class="form group">
			<label for="password">Ваш password:</label>
			<input type ="password" class="form-control" id="password" placeholder="Введите password:" required v-model="user.password">
		</div>
		<button type="submit" class="btn btn-primary">Войти</button>
	</form>
</template>


<script>
    import $ from 'jquery'
	export default {
	    name: 'SignIn',
		data(){
			return {
				user: {
					email: '',
					password: '',
					username: ''
				}
			}
		},
		methods: {
			enterUser() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/jwt/create/',
                    type: 'POST',
                    data: {
                        username: this.user.email,
                        password: this.user.password,
                        username: this.user.username
                    },
                    success: (response) => {
                        console.log(response.access)
                        localStorage.setItem('auth_key', response.access);
                        localStorage.setItem('authentication', true);
                        this.$router.push({name: 'Home'})
                    },
                    error: (response) => {
                        if (response.status === 401) {
                            alert('логин или пароль неверный')
                        }
                    }
                })
			},
		},
	}
</script>

<style>
    .form-group {
        position: absolute

    }
    .btn btn-primary {
        margin-left: 5 px
    }


</style>
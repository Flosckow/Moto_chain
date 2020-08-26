<template>
	<form class="mt-5" @submit.prevent="registerUser">
		<div class="align-self-center">
		    <label for="text">Регистарция</label>
		</div>
		<div class="form group">
			<label for="password">Ваш username:</label>
			<input type ="text" class="form-control" id="username" placeholder="Введите username:" required v-model="user.username">
		</div>
		<div class="form group">
			<label for="email">Ваш email:</label>
			<input type ="email" class="form-control" id="email" placeholder="Введите email:"  v-model="user.email">
		</div>
		<div class="form group">
			<label for="password">Ваш password:</label>
			<input type ="password" class="form-control"
			 id="password" placeholder="Введите password:"
			 v-model="user.password">
		</div>
		<div class="form group">
			<label for="password2">Подтвердите password:</label>
			<input type ="password" @blur="$v.user.confirmPassword.$touch()" :class="{'is-invalid': $v.user.confirmPassword.$error}" class="form-control" id="confirmPassword"
			placeholder="Введите password:"  v-model="user.confirmPassword">
		</div>
		<div :class="{'is-invalid': $v.user.confirmPassword.$error}">
		    <small>Пароли должны совпадать</small>
		</div>
		<button type="submit" class="btn btn-primary">Зарегистрироваться</button>
	</form>
</template>


<script>
    import { required , sameAs, minLength} from 'vuelidate/lib/validators';
    import moment from 'moment';
    import $ from 'jquery'
	export default {
	    name: 'SignUp',
		data(){
			return {
				user: {
					email: '',
					password: '',
					confirmPassword: '',
					username: '',
				}
			}
		},
		validations: {
		    user: {
		        password: {
                    required,
                    minLength: minLength(6)
                },
                    confirmPassword: { required, sameAsPassword: sameAs('password') }
		    }
		},
		methods: {
			registerUser() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/users/',
                    type: 'POST',
                    data: {
                        email: this.user.email,
                        password: this.user.password,
                        confirmPassword: this.user.confirmPassword,
                        username: this.user.username
                    },
                    success: (response) => {
                        // this.$router.push({name: 'login'})
                        console.log(response)
                        console.log(user)
                    },
                    error: (response) => {
                        if (this.response === 400)
                            alert('Произошла ошибка')
                    }
                })
			}
		}
	}
</script>


<style scoped>
    .error {
        color: red;
    }
</style>
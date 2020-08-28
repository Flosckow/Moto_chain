<template>
        <div class="container py-md-4">
            <div class="row">
                <div class="left-ads-display col-lg-9">
                            <div class="row">
                                <div v-for="product in cart" :key="product.id" class="col-md-4 product-men">
                                    <div class="product-shoe-info editContent text-center mt-lg-4">
                                        <div class="item-info-product">
                                            <h4 class="">
                                                <a href="#" class="editContent"><img class='img-cart' :src='product.product.image'></a>
                                            </h4>
                                            <div class="customText">
                                                <span class="money editContent"> Название: {{product.product.title}} </span>
                                            </div>
                                            <div class="product_price">
                                                <div class="grid-price">
                                                    <span class="money editContent"> Цена: {{product.sum_price}} $</span>
                                                </div>
                                            </div>
                                            <div class="product_price">
                                                <div class="grid-price">
                                                    <span class="money editContent"> Количество: {{product.quantity}} </span>
                                                </div>
                                            </div>
                                            <button class="login" @click="removeItemFromCart(product)"> Удалить</button>
                                        </div>
                                    </div>

                                </div>
                            </div>
                 </div>
            </div>
        <tr>
           <td><b class ="customText"> Total price: $</b></td>
           <td></td>
           <td><b  class ="customText">{{cartTotalCost}}</b></td>
        </tr>
        <tr>
           <td><b><button class="login">Заказать</button></b></td>
        </tr>
        </div>
</template>

<script>
    import options from '../headers.js'

    export default {
        name: "Cart",
        data() {
            return {
                cart: [],
                product: {},
            }
        },
        created() {
            this.loadCartItem()
        },
        methods: {
            async loadCartItem() {
                this.cart = await fetch(
                    `${this.$store.getters.getServerUrl}api/cart/cart/`, options
                ).then(response => response.json()
                ).then(response => {
                    this.total = response.count
                    return response.results
                    console.log(cart)
                })
            },
            removeItemFromCart(product) {
                this.cart.splice(this.cart.indexOf(product)) // исправить на след строке, необходим сам счетчик корзины
                fetch(`${this.$store.getters.getServerUrl}api/cart/delete/${product.id}/`, {
                    method: 'DELETE',
                    ...options,
                })
                .then(response => response.json())
                .then(function (data) {
                    console.log('Request succeeded with JSON response', data);
                    console.log(product)
                })
                .catch(function (error) {
                    console.log('Request failed', error);
                });
            },
        },
        computed: {
            cartTotalCost() {
                return this.cart.reduce((total, product) => total + product.sum_price, 0);
            }
        }
    }
</script>

<style scoped>
    .single {
        outline: none;
        outline-offset: -2px;
        cursor: inherit;
        color: rgb(33, 37, 41);
        font-size: 16px;
        background-color: rgba(0, 0, 0, 0);
        font-family: Lato, sans-serif;
    }
    .li-movie{
        list-style: none;
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
    .rightcol {
     position: absolute; /* Абсолютное позиционирование */
     top: 20px; /* Положение от верхнего края */
     right: 10px; /* Положение от правого края */
     width: 200px; /* Ширина блока */
     background: #ccc; /* Цвет фона */
     border: 1px solid black; /* Параметры рамки */
     padding: 10px; /* Поля вокруг текста */
    }

    .customText {
        color: #111;
        font-family: ‘Helvetica Neue’, sans-serif;
        font-size: 20px;
        font-weight: bold;
        letter-spacing: -1px;
        line-height: 1; text-align: center;
    }
    .img-cart {
        width:100%

    }

</style>
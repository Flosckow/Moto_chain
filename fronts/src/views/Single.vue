<template>
    <section class="ab-info-main py-md-5 py-4 editContent single">
        <div class="container py-md-4">
            <div class="row">
                <div class="left-ads-display col-lg-10">
                    <div class="row">
                        <div class="desc1-left col-md-6">
                            <img :src="product.image" class="img-fluid" alt="">
                        </div>
                        <div class="desc1-right col-md-6 pl-lg-4">
                            <h3 class="editContent">{{product.title}}</h3>
                            <ul>
                                <li class="li-movie"><span><b>Описание:</b> {{product.description}}</span>
                                </li>
                                <li class="li-movie"><span><b>Категория:</b>{{product.category}}</span>
                                </li>
                                <li class="li-movie"><span><b>Цена:</b>{{product.price}}</span>
                                </li>
                                <div class="share-desc">
                                    <div class="share">
                                        <ul class="w3layouts_social_list list-unstyled">
                                            <li><button @click="addItemToCart(product)" class="login">Add to Cart</button>
                                                </a>
                                            </li>
                                        </ul>
                                    </div>
                                    <div class="clearfix"></div>
                                </div>
                            </ul>
                        </div>
                    </div>
                    <hr>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    import options from '../headers.js'
    export default {
        name: "Single",
        props: ['id'],
        data() {
            return {
                cart: {},
                product: {},
            }
        },
        created() {
            this.loadProduct()
        },
        methods: {
            async loadProduct() {
                this.product = await fetch(
                    `${this.$store.getters.getServerUrl}api/order/${this.id}`
                ).then(response => response.json())
            },
            async loadCart() {
                this.product = await fetch(
                    `${this.$store.getters.getServerUrl}api/cart/add-cart-item/${this.id}/`
                ).then(response => response.json())
            },
            addItemToCart(product, cart) {
                let itemCart = {
                    product: product.id,
                    quantity: product.quantity,
                    price: product.sum_price,
                    name: product.title
                }
                fetch(`${this.$store.getters.getServerUrl}api/cart/add-cart-item/${this.id}/`, {
                    method: 'POST',
                    ...options,
                    body: JSON.stringify(itemCart)
                })
                .then(response => response.json())
                .then(function (data) {
                    console.log('Request succeeded with JSON response', data);
                    console.log(cart);
                })
                .catch(function (error) {
                    console.log('Request failed', error);
                });
            },
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
</style>
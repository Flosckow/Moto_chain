<template>
    <div class="home">
        <section class="ab-info-main py-md-5 py-4 editContent">
            <div class="container-fluid py-md-3">
                <div class="row">
                    <div class="side-bar col-lg-3">
                        <div class="search-bar w3layouts-newsletter">
                            <h3 class="sear-head editContent">Поиск мото</h3>
                            <form action="#" method="get" class="d-flex editContent">
                                <input type="search" placeholder="Введите название..." name="search"
                                       class="form-control" required="" v-model.trim="search" @keyup="getAllStarWarsPeople">
                                <ul>
                                    <li v-for="product in listProduct" :key="product.id" visibility: hidden>{{ product.title }}</li>
                                </ul>
                            </form>
                        </div>


                        <div class="left-side my-4">
                            <h3 class="sear-head editContent">Класс</h3>
                            <ul class="w3layouts-box-list">
                                <li class="editContent">
                                    <input type="checkbox" class="checked" v-model.trim="category" name='class' @click="sortModel" id=1>
                                    <span class="span editContent">sport</span>
                                    <ul>
                                        <li v-for="product in listProduct" :key="product.id" visibility: hidden>{{ product.category }}</li>
                                    </ul>
                                </li>
                                <li class="editContent">
                                    <input type="checkbox" class="checked" name='class' v-model='category' value="street" id=3 @click='sortModel'>
                                    <span class="span editContent">Street</span>
                                </li>
                                <li class="editContent">
                                    <input type="checkbox" name='class' class="checked">
                                    <span class="span editContent">OffRoad</span>
                                </li>
                                <li class="editContent">
                                    <input type="checkbox" class="checked" name='class' value="tourist" id=2 @click='sortModel'>
                                    <span class="span editContent">Tourist</span>
                                </li>
                            </ul>
                        </div>


                        <div class="left-side">
                            <h3 class="sear-head editContent">Цена</h3>
                            <ul class="w3layouts-box-list">
                                <li class="editContent">
                                    <input type="checkbox" name="price" class="checked">
                                    <span class="span editContent">до 150000</span>
								</li>
                            </ul>
							<ul class="w3layouts-box-list">
                                <li class="editContent">
                                    <input type="checkbox" name="price" class="checked">
                                    <span class="span editContent">150000-300000</span>
								</li>
                            </ul>
							<ul class="w3layouts-box-list">
                                <li class="editContent">
                                    <input type="checkbox" name="price" class="checked">
                                    <span class="span editContent">300000-450000</span>
								</li>
							</ul>
							<ul class="w3layouts-box-list">
                                <li class="editContent">
                                    <input type="checkbox" name="price" class="checked">
                                    <span class="span editContent">450000 выше</span>
								</li>
							</ul>
                        </div>
                            
                        <div class="deal-leftmk left-side">
                            <h3 class="sear-head editContent">Популярное</h3>
                            <div class="special-sec1 row mt-3 editContent">
                                <div class="img-deals col-md-4">
                                    <img src="./../assets/images/ducati_panigalle.jpg" class="img-fluid" alt="">
                                </div>
                                <div class="img-deal1 col-md-4">
                                    <h3 class="editContent">Ducati Panigalle v4</h3>
                                    <a href="moviesingle.html" class="editContent"></a>
                                </div>

                            </div>
                            <div class="special-sec1 row mt-3 editContent">
                                <div class="img-deals col-md-4">
                                    <img src="./../assets/images/Yamaxa_mt10.jpg" class="img-fluid" alt="">
                                </div>
                                <div class="img-deal1 col-md-8">
                                    <h3 class="editContent">Yamaxa mt-10</h3>
                                    <a href="moviesingle.html" class="editContent"></a>
                                </div>

                            </div>
                            <div class="special-sec1 row mt-3 editContent">
                                <div class="img-deals col-md-4">
                                    <img src="./../assets/images/Harley-Davidson_Fatboy.jpg" class="img-fluid" alt="">
                                </div>
                                <div class="img-deal1 col-md-8">
                                    <h3 class="editContent">Harley Davidson Fat Boy 114</h3>
                                    <a href="moviesingle.html" class="editContent"></a>
                                </div>

                            </div>
                            <div class="special-sec1 row mt-3 editContent">
                                <div class="img-deals col-md-4">
                                    <img src="./../assets/images/Suzuki.jpg" class="img-fluid" alt="">
                                </div>
                                <div class="img-deal1 col-md-8">
                                    <h3 class="editContent">Suzuki GSXR</h3>
                                    <a href="moviesingle.html" class="editContent"></a>
                                </div>
                            </div>
                        </div>
                        <!-- //deals -->
                    </div>


                    <div class="left-ads-display col-lg-9">
                        <div class="row">
                            <div v-for="product in listProduct" :key="product.id" class="col-md-4 product-men">
                                <div class="product-shoe-info editContent text-center mt-lg-4">
                                    <div class="item-info-product">
                                        <div class="desc1-left col-md-6">
                                            <img :src="product.image" class="img-fluid" image-rendering:auto alt="">
                                        </div>
                                        <h4 class="">
                                            <a href="#" @click="goTo(product.id)" class="editContent">{{ product.title }}</a>
                                        </h4>

                                        <div class="product_price">
                                            <div class="grid-price">
                                                <span class="money editContent"> Цена: {{product.price}} $</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
    import Pagination from "../components/Pagination";
    export default {
        name: 'Home',
        data() {
            return {
                listProduct: [],
                page: '',
                total: 0,
                search: '',
                category: '',

            }
        },
        components: {Pagination},
        methods: {
            async loadListProducts(pageNumber) {
                this.listProduct = await fetch(
                    `${this.$store.getters.getServerUrl}api/order?${pageNumber}`
                ).then(response => response.json()
                ).then(response => {
                    this.total = response.count
                    return response.results
                })
            },
            goTo(id) {
                this.$router.push({ name: 'Single', params: {id: id} })
            },
            getAllStarWarsPeople() {
                fetch(`${this.$store.getters.getServerUrl}api/order/?search=${this.search}`)
                    .then(response => response.json())
                    .then(res => {
                        if (this.search) {
                            this.listProduct = res.results.filter(product =>
                                product.title.toLowerCase().includes(this.search.toLowerCase())
                            );
                        } else {
                            this.listProduct = res.results;
                        }
                    });
            },
            sortModel () {
                fetch(`${this.$store.getters.getServerUrl}api/category/?category=1`)
                    .then(response => response.json())
                    .then(res => {
                        if (this.category) {
                            this.listProduct = res.results.filter(product =>
                                product.category.includes(this.category)
                            );
                        } else {
                            this.listProduct = res.results;
                        }
                    });
            },
        },
        created() {
            this.loadListProducts(this.page)
        },
        mounted() {
            this.sortModel();
        },


    }
</script>

<style scoped>
    .editContent {
        padding-left: 3rem;
        padding-right: 3rem;
    }
</style>
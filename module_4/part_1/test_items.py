link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestItemMarket:
    def test_button_to_basket(self, browser):
        btn_add_to_basket = ".btn-add-to-basket"
        text_btn_add_to_basket = ["Добавить в корзину",
                                  "أضف الى سلة التسوق",
                                  "Afegeix a la cistella",
                                  "Vložit do košíku",
                                  "Læg i kurv",
                                  "In Warenkorb legen",
                                  "Add to basket",
                                  "Προσθήκη στο καλάθι",
                                  "Añadir al carrito",
                                  "Lisää koriin",
                                  "Ajouter au panier",
                                  "Aggiungi al carrello",
                                  "장바구니 담기",
                                  "Voeg aan winkelmand toe",
                                  "Dodaj do koszyka",
                                  "Adicionar ao carrinho",
                                  "Adicionar à cesta",
                                  "Adauga in cos",
                                  "Pridať do košíka",
                                  "Додати в кошик",
                                 ]


        browser.get(link)
        browser.implicitly_wait(5)
        btn_text = browser.find_element_by_css_selector(btn_add_to_basket).text


        assert (btn_text in text_btn_add_to_basket) == True, "кнопка не содержит нужный текст"



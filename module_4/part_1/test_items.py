link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestItemMarket:
    def test_button_to_basket(self, browser, language):
        # Arrange
        btn_add_to_basket = ".btn-add-to-basket"
        text_btn_add_to_basket = {"ru": "Добавить в корзину",
                                  "ar": "أضف الى سلة التسوق",
                                  "ca": "Afegeix a la cistella",
                                  "cs": "Vložit do košíku",
                                  "da": "Læg i kurv",
                                  "de": "In Warenkorb legen",
                                  "en-gb": "Add to basket",
                                  "el": "Προσθήκη στο καλάθι",
                                  "es": "Añadir al carrito",
                                  "fi": "Lisää koriin",
                                  "fr": "Ajouter au panier",
                                  "it": "Aggiungi al carrello",
                                  "ko": "장바구니 담기",
                                  "nl": "Voeg aan winkelmand toe",
                                  "pl": "Dodaj do koszyka",
                                  "pt": "Adicionar ao carrinho",
                                  "pt-br": "Adicionar à cesta",
                                  "ro": "Adauga in cos",
                                  "sk": "Pridať do košíka",
                                  "uk": "Додати в кошик",
                                  }

        # Act
        browser.get(link)
        browser.implicitly_wait(5)
        btn_text = browser.find_element_by_css_selector(btn_add_to_basket).text

        # Assert
        assert (btn_text in text_btn_add_to_basket[language]) == True, "кнопка не содержит нужный текст"

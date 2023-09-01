public class CashProvider {
    private long card;
    private long hashCard;
    private boolean isAuthorization;

    public CashProvider(long card, long hashCard) {
        this.card = card;
        this.hashCard = hashCard;
        this.isAuthorization = false;
    }
    // Авторизация
    public void authorization(Customer customer) {
        isAuthorization = true;
    }
// Логика покупки билетов
    public void buy(double price) {
        if (isAuthorization && cardHasFunds(price)) {

        } else {
            
        }
    }
// Проверка наличия денежных средств
    public boolean cardHasFunds(double amount) {
        
        return true;
    }
}
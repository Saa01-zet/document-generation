class DocumentLogger:
    _instance = None
    _total_logs = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message: str) -> None:
        self._total_logs += 1
        print(f"[LOG] {message}")

    def get_stats(self) -> dict:
        return {"total_logs": self._total_logs}


class InvoiceDocument:
    def generate(self, customer: str, amount: int) -> str:
        DocumentLogger().log(f"Создан счёт для {customer}")
        return f"СЧЁТ\nКлиент: {customer}\nСумма: {amount}"


class ReceiptDocument:
    def generate(self, customer: str, amount: int) -> str:
        DocumentLogger().log(f"Создан чек для {customer}")
        return f"ЧЕК\nПокупатель: {customer}\nОплачено: {amount}"


def create_document(format: str) -> "Document":
    if format == "invoice":
        return InvoiceDocument()
    elif format == "receipt":
        return ReceiptDocument()
    else:
        raise ValueError(f"Неизвестный формат документа: {format}")

if __name__ == "__main__":
    doc1 = create_document("invoice")
    print(doc1.generate("Иван", 1500))

    doc2 = create_document("receipt")
    print(doc2.generate("Анна", 800))

    print(DocumentLogger().get_stats())
    print(DocumentLogger() is DocumentLogger())
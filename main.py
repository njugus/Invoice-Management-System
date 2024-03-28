class Client:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Client: {self.name}, Address: {self.address}"


class Invoice:
    def __init__(self, client, invoice_number, amount):
        self.client = client
        self.invoice_number = invoice_number
        self.amount = amount

    def __str__(self):
        return f"Invoice {self.invoice_number} - Amount: ${self.amount:.2f} - Client: {self.client.name}"


class InvoiceManagementSystem:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def remove_invoice(self, invoice_number):
        for invoice in self.invoices:
            if invoice.invoice_number == invoice_number:
                self.invoices.remove(invoice)
                return True
        return False

    def get_invoices_by_client(self, client_name):
        client_invoices = []
        for invoice in self.invoices:
            if invoice.client.name == client_name:
                client_invoices.append(invoice)
        return client_invoices


# Example usage:
if __name__ == "__main__":
    # Creating clients
    client1 = Client("Client A", "123 Main St")
    client2 = Client("Client B", "456 Park Ave")

    # Creating invoices
    invoice1 = Invoice(client1, "001", 1000)
    invoice2 = Invoice(client2, "002", 1500)

    # Creating invoice management system
    invoice_system = InvoiceManagementSystem()

    # Adding invoices to the system
    invoice_system.add_invoice(invoice1)
    invoice_system.add_invoice(invoice2)

    # Displaying all invoices
    print("All Invoices:")
    for invoice in invoice_system.invoices:
        print(invoice)

    # Removing an invoice
    invoice_system.remove_invoice("001")

    # Displaying all invoices after removal
    print("\nInvoices after removal:")
    for invoice in invoice_system.invoices:
        print(invoice)

    # Getting invoices by client
    print("\nInvoices for Client B:")
    client_b_invoices = invoice_system.get_invoices_by_client("Client B")
    for invoice in client_b_invoices:
        print(invoice)

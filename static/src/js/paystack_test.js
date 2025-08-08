import { PaymentInterface } from "@point_of_sale/app/payment/payment_interface";

export class PaystackTestPayment extends PaymentInterface {
  send_payment_request(cid) {
    console.log("Test payment request");
    return Promise.resolve(true);
  }
}

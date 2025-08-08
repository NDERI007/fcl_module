/** @odoo-module **/
import { registry } from "@web/core/registry";
import { PaystackTestPayment } from "./paystack_test";

console.log("Registering paystack payment method...");
registry
  .category("pos_payment_methods")
  .add("payment_method_paystack", PaystackTestPayment);

console.log("Paystack payment method registered!");

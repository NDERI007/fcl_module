/** @odoo-module **/
import { PosGlobalState } from "@point_of_sale/app/models/pos_global_state";
import { PaystackTestPayment } from "./paystack_test";

console.log("Registering paystack payment method...");
PosGlobalState.addPaymentMethod("Paystack", PaystackTestPayment);
console.log("Paystack payment method registered!");

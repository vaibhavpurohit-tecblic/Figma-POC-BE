static_html_data = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
  <style>@import url("https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css");
    @import url("https://fonts.googleapis.com/css?family=Poppins:400");
    * {
      -webkit-font-smoothing: antialiased;
      box-sizing: border-box;
    }
    html,
    body {
      margin: 0px;
      height: 100%;
    }
    /* a blue color as a generic focus style */
    button:focus-visible {
      outline: 2px solid #4a90e2 !important;
      outline: -webkit-focus-ring-color auto 5px !important;
    }
    a {
      text-decoration: none;
    }
    .sign-up-step {
  background-color: #0a1530;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.sign-up-step .div {
  background-color: #0a1530;
  width: 1440px;
  height: 1024px;
  position: relative;
}

.sign-up-step .frame {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;
  padding: 24px 40px;
  position: absolute;
  top: 216px;
  left: 433px;
  background-color: #ffffff;
  box-shadow: 0px 2px 4px -2px #ffffff0f, 0px 4px 8px -2px #ffffff1a;
}

.sign-up-step .frame-2 {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  position: relative;
  flex: 0 0 auto;
}

.sign-up-step .frame-3 {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  position: relative;
  flex: 0 0 auto;
}

.sign-up-step .text-wrapper {
  position: relative;
  width: fit-content;
  margin-top: -1px;
  font-family: var(--body-2-semibold-font-family);
  font-weight: var(--body-2-semibold-font-weight);
  color: var(--texttext-black-second);
  font-size: var(--body-2-semibold-font-size);
  text-align: center;
  letter-spacing: var(--body-2-semibold-letter-spacing);
  line-height: var(--body-2-semibold-line-height);
  white-space: nowrap;
  font-style: var(--body-2-semibold-font-style);
}

.sign-up-step .text-wrapper-2 {
  position: relative;
  width: 457px;
  font-family: var(--heading-2-semibold-font-family);
  font-weight: var(--heading-2-semibold-font-weight);
  color: var(--texttext-black);
  font-size: var(--heading-2-semibold-font-size);
  text-align: center;
  letter-spacing: var(--heading-2-semibold-letter-spacing);
  line-height: var(--heading-2-semibold-line-height);
  font-style: var(--heading-2-semibold-font-style);
}

.sign-up-step .text-wrapper-3 {
  position: relative;
  align-self: stretch;
  font-family: var(--body-2-regular-font-family);
  font-weight: var(--body-2-regular-font-weight);
  color: var(--texttext-black-second);
  font-size: var(--body-2-regular-font-size);
  text-align: center;
  letter-spacing: var(--body-2-regular-letter-spacing);
  line-height: var(--body-2-regular-line-height);
  font-style: var(--body-2-regular-font-style);
}

.sign-up-step .frame-4 {
  display: inline-flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 16px;
  position: relative;
  flex: 0 0 auto;
}

.sign-up-step .frame-5 {
  display: flex;
  width: 494px;
  height: 48px;
  align-items: center;
  gap: 8px;
  padding: 0px 12px;
  position: relative;
  background-color: var(--basewhite);
  border-radius: 8px;
  border: 1px solid;
  border-color: var(--neutral-300);
}

.sign-up-step .text-wrapper-4 {
  position: relative;
  flex: 1;
  font-family: var(--body-2-regular-font-family);
  font-weight: var(--body-2-regular-font-weight);
  color: var(--texttext-black);
  font-size: var(--body-2-regular-font-size);
  letter-spacing: var(--body-2-regular-letter-spacing);
  line-height: var(--body-2-regular-line-height);
  font-style: var(--body-2-regular-font-style);
}

.sign-up-step .radio-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  position: relative;
  flex: 0 0 auto;
}

.sign-up-step .radio-button-2 {
  position: relative;
  width: 20px;
  height: 20px;
  background-color: #ffffff;
  border-radius: 10px;
  border: 1px solid;
  border-color: #cdd4de;
}

.sign-up-step .button {
  all: unset;
  box-sizing: border-box;
  display: flex;
  width: 250px;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px 16px;
  position: relative;
  flex: 0 0 auto;
  background-color: var(--infomain-500);
  border-radius: 3px;
}

.sign-up-step .input-text {
  position: relative;
  width: fit-content;
  margin-top: -1px;
  font-family: var(--body-2-semibold-font-family);
  font-weight: var(--body-2-semibold-font-weight);
  color: #ffffff;
  font-size: var(--body-2-semibold-font-size);
  letter-spacing: var(--body-2-semibold-letter-spacing);
  line-height: var(--body-2-semibold-line-height);
  white-space: nowrap;
  font-style: var(--body-2-semibold-font-style);
}

.sign-up-step .header {
  position: absolute;
  width: 1440px;
  height: 86px;
  top: 0;
  left: 0;
  background-color: #ffffff;
  border-top-style: none;
  border-right-style: none;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-left-style: none;
  border-color: var(--neutral-300);
}

.sign-up-step .group {
  position: absolute;
  width: 52px;
  height: 50px;
  top: 18px;
  left: 100px;
}

.sign-up-step .overlap-group {
  position: relative;
  width: 50px;
  height: 50px;
  background-color: #0a1530;
  border-radius: 25px;
}

.sign-up-step .text-wrapper-5 {
  position: absolute;
  top: 8px;
  left: 17px;
  font-family: "Poppins", Helvetica;
  font-weight: 400;
  color: #ffffff;
  font-size: 22px;
  letter-spacing: -0.22px;
  line-height: 32.9px;
  white-space: nowrap;
}

.sign-up-step .button-2 {
  all: unset;
  box-sizing: border-box;
  display: flex;
  width: 130px;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 9px 16px;
  position: absolute;
  top: 24px;
  left: 1230px;
  background-color: var(--basewhite);
  border-radius: 3px;
  border: 1px solid;
  border-color: var(--secondarymain-500);
}

.sign-up-step .input-text-2 {
  position: relative;
  width: fit-content;
  margin-top: -1px;
  font-family: var(--caption-1-medium-font-family);
  font-weight: var(--caption-1-medium-font-weight);
  color: var(--secondarymain-500);
  font-size: var(--caption-1-medium-font-size);
  letter-spacing: var(--caption-1-medium-letter-spacing);
  line-height: var(--caption-1-medium-line-height);
  white-space: nowrap;
  font-style: var(--caption-1-medium-font-style);
}
:root {
  --basefill-disabled: rgba(237, 237, 237, 1);
  --basetext-disabled: rgba(158, 158, 158, 1);
  --baseblack: rgba(0, 0, 0, 1);
  --basewhite: rgba(255, 255, 255, 1);
  --texttertiary: rgba(235, 235, 235, 1);
  --textsecond: rgba(241, 241, 241, 1);
  --textmain: rgba(255, 255, 255, 1);
  --texttext-black: rgba(21, 21, 21, 1);
  --texttext-black-second: rgba(85, 85, 85, 1);
  --texttext-black-third: rgba(119, 119, 119, 1);
  --neutral-900: rgba(18, 25, 38, 1);
  --neutral-800: rgba(32, 41, 57, 1);
  --neutral-700: rgba(54, 65, 82, 1);
  --neutral-600: rgba(75, 85, 101, 1);
  --neutral-500: rgba(105, 117, 134, 1);
  --neutral-400: rgba(154, 164, 178, 1);
  --neutral-300: rgba(205, 213, 223, 1);
  --neutral-200: rgba(227, 232, 239, 1);
  --neutral-100: rgba(238, 242, 246, 1);
  --neutral-50: rgba(248, 250, 252, 1);
  --neutral-25: rgba(252, 252, 253, 1);
  --primaryfocused-400: rgba(218, 221, 227, 1);
  --primarypressed-800: rgba(10, 21, 39, 1);
  --primaryhover-700: rgba(19, 39, 74, 1);
  --primaryborder-300: rgba(132, 146, 160, 1);
  --primarysurface-100: rgba(237, 244, 255, 1);
  --primarymain-600: rgba(26, 54, 104, 1);
  --secondaryfocused-400: rgba(214, 223, 247, 1);
  --secondarypressed-800: rgba(46, 69, 127, 1);
  --secondaryhover-700: rgba(61, 92, 170, 1);
  --secondaryborder-300: rgba(119, 157, 255, 1);
  --secondarysurface-50: rgba(235, 241, 255, 1);
  --secondarymain-500: rgba(0, 140, 220, 1);
  --successfocused-400: rgba(200, 232, 216, 1);
  --successpressed-800: rgba(9, 92, 55, 1);
  --successhover-700: rgba(8, 116, 67, 1);
  --successborder-300: rgba(115, 226, 163, 1);
  --successsurface-50: rgba(237, 252, 242, 1);
  --successmain-500: rgba(22, 179, 100, 1);
  --warningfocused-400: rgba(241, 228, 196, 1);
  --warningpressed-800: rgba(112, 80, 0, 1);
  --warninghover-700: rgba(149, 107, 0, 1);
  --warningborder-300: rgba(229, 177, 42, 1);
  --warningsurface-50: rgba(255, 248, 229, 1);
  --warningmain-500: rgba(224, 161, 0, 1);
  --errorfocused-400: rgba(244, 210, 207, 1);
  --errorpressed-800: rgba(145, 32, 24, 1);
  --errorhover-700: rgba(180, 35, 24, 1);
  --errorborder-300: rgba(253, 162, 155, 1);
  --errorsurface-50: rgba(254, 243, 242, 1);
  --errormain-500: rgba(240, 68, 56, 1);
  --infomain-500: rgba(0, 140, 220, 1);
  --infoborder-300: rgba(119, 157, 255, 1);
  --infopressed-800: rgba(46, 69, 127, 1);
  --price-list-font-family: "SatoshiVariable-Medium", Helvetica;
  --price-list-font-weight: 500;
  --price-list-font-size: 16px;
  --price-list-letter-spacing: -0.32px;
  --price-list-line-height: 139.9999976158142%;
  --price-list-font-style: normal;
  --display-1-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --display-1-bold-font-weight: 700;
  --display-1-bold-font-size: 72px;
  --display-1-bold-letter-spacing: -2.88px;
  --display-1-bold-line-height: 120.00000476837158%;
  --display-1-bold-font-style: normal;
  --display-1-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --display-1-semibold-font-weight: 500;
  --display-1-semibold-font-size: 72px;
  --display-1-semibold-letter-spacing: -2.88px;
  --display-1-semibold-line-height: 120.00000476837158%;
  --display-1-semibold-font-style: normal;
  --display-1-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --display-1-medium-font-weight: 500;
  --display-1-medium-font-size: 72px;
  --display-1-medium-letter-spacing: -2.88px;
  --display-1-medium-line-height: 120.00000476837158%;
  --display-1-medium-font-style: normal;
  --display-1-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --display-1-regular-font-weight: 400;
  --display-1-regular-font-size: 72px;
  --display-1-regular-letter-spacing: -2.88px;
  --display-1-regular-line-height: 120.00000476837158%;
  --display-1-regular-font-style: normal;
  --display-1-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --display-1-thin-font-weight: 300;
  --display-1-thin-font-size: 72px;
  --display-1-thin-letter-spacing: -2.88px;
  --display-1-thin-line-height: 120.00000476837158%;
  --display-1-thin-font-style: normal;
  --display-2-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --display-2-bold-font-weight: 700;
  --display-2-bold-font-size: 54px;
  --display-2-bold-letter-spacing: -1.62px;
  --display-2-bold-line-height: 120.00000476837158%;
  --display-2-bold-font-style: normal;
  --display-2-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --display-2-semibold-font-weight: 500;
  --display-2-semibold-font-size: 54px;
  --display-2-semibold-letter-spacing: -1.62px;
  --display-2-semibold-line-height: 120.00000476837158%;
  --display-2-semibold-font-style: normal;
  --display-2-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --display-2-medium-font-weight: 500;
  --display-2-medium-font-size: 54px;
  --display-2-medium-letter-spacing: -1.62px;
  --display-2-medium-line-height: 120.00000476837158%;
  --display-2-medium-font-style: normal;
  --display-2-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --display-2-regular-font-weight: 400;
  --display-2-regular-font-size: 54px;
  --display-2-regular-letter-spacing: -1.62px;
  --display-2-regular-line-height: 120.00000476837158%;
  --display-2-regular-font-style: normal;
  --display-2-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --display-2-thin-font-weight: 300;
  --display-2-thin-font-size: 54px;
  --display-2-thin-letter-spacing: -1.62px;
  --display-2-thin-line-height: 120.00000476837158%;
  --display-2-thin-font-style: normal;
  --heading-1-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --heading-1-bold-font-weight: 700;
  --heading-1-bold-font-size: 48px;
  --heading-1-bold-letter-spacing: -1.44px;
  --heading-1-bold-line-height: 120.00000476837158%;
  --heading-1-bold-font-style: normal;
  --heading-1-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-1-semibold-font-weight: 500;
  --heading-1-semibold-font-size: 48px;
  --heading-1-semibold-letter-spacing: -1.44px;
  --heading-1-semibold-line-height: 120.00000476837158%;
  --heading-1-semibold-font-style: normal;
  --heading-1-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-1-medium-font-weight: 500;
  --heading-1-medium-font-size: 48px;
  --heading-1-medium-letter-spacing: -1.44px;
  --heading-1-medium-line-height: 120.00000476837158%;
  --heading-1-medium-font-style: normal;
  --heading-1-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --heading-1-regular-font-weight: 400;
  --heading-1-regular-font-size: 48px;
  --heading-1-regular-letter-spacing: -1.44px;
  --heading-1-regular-line-height: 120.00000476837158%;
  --heading-1-regular-font-style: normal;
  --heading-1-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --heading-1-thin-font-weight: 300;
  --heading-1-thin-font-size: 48px;
  --heading-1-thin-letter-spacing: -1.44px;
  --heading-1-thin-line-height: 120.00000476837158%;
  --heading-1-thin-font-style: normal;
  --heading-2-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --heading-2-bold-font-weight: 700;
  --heading-2-bold-font-size: 38px;
  --heading-2-bold-letter-spacing: -0.76px;
  --heading-2-bold-line-height: 120.00000476837158%;
  --heading-2-bold-font-style: normal;
  --heading-2-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-2-semibold-font-weight: 500;
  --heading-2-semibold-font-size: 38px;
  --heading-2-semibold-letter-spacing: -0.76px;
  --heading-2-semibold-line-height: 120.00000476837158%;
  --heading-2-semibold-font-style: normal;
  --heading-2-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-2-medium-font-weight: 500;
  --heading-2-medium-font-size: 38px;
  --heading-2-medium-letter-spacing: -0.76px;
  --heading-2-medium-line-height: 120.00000476837158%;
  --heading-2-medium-font-style: normal;
  --heading-2-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --heading-2-regular-font-weight: 400;
  --heading-2-regular-font-size: 38px;
  --heading-2-regular-letter-spacing: -0.76px;
  --heading-2-regular-line-height: 120.00000476837158%;
  --heading-2-regular-font-style: normal;
  --heading-2-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --heading-2-thin-font-weight: 300;
  --heading-2-thin-font-size: 38px;
  --heading-2-thin-letter-spacing: -0.76px;
  --heading-2-thin-line-height: 120.00000476837158%;
  --heading-2-thin-font-style: normal;
  --heading-3-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --heading-3-bold-font-weight: 700;
  --heading-3-bold-font-size: 32px;
  --heading-3-bold-letter-spacing: -0.64px;
  --heading-3-bold-line-height: 120.00000476837158%;
  --heading-3-bold-font-style: normal;
  --heading-3-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-3-semibold-font-weight: 500;
  --heading-3-semibold-font-size: 32px;
  --heading-3-semibold-letter-spacing: -0.64px;
  --heading-3-semibold-line-height: 120.00000476837158%;
  --heading-3-semibold-font-style: normal;
  --heading-3-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-3-medium-font-weight: 500;
  --heading-3-medium-font-size: 32px;
  --heading-3-medium-letter-spacing: -0.64px;
  --heading-3-medium-line-height: 120.00000476837158%;
  --heading-3-medium-font-style: normal;
  --heading-3-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --heading-3-regular-font-weight: 400;
  --heading-3-regular-font-size: 32px;
  --heading-3-regular-letter-spacing: -0.64px;
  --heading-3-regular-line-height: 120.00000476837158%;
  --heading-3-regular-font-style: normal;
  --heading-3-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --heading-3-thin-font-weight: 300;
  --heading-3-thin-font-size: 32px;
  --heading-3-thin-letter-spacing: -0.64px;
  --heading-3-thin-line-height: 120.00000476837158%;
  --heading-3-thin-font-style: normal;
  --heading-4-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --heading-4-bold-font-weight: 700;
  --heading-4-bold-font-size: 28px;
  --heading-4-bold-letter-spacing: -0.56px;
  --heading-4-bold-line-height: 110.00000238418579%;
  --heading-4-bold-font-style: normal;
  --heading-4-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-4-semibold-font-weight: 500;
  --heading-4-semibold-font-size: 28px;
  --heading-4-semibold-letter-spacing: -0.56px;
  --heading-4-semibold-line-height: 110.00000238418579%;
  --heading-4-semibold-font-style: normal;
  --heading-4-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-4-medium-font-weight: 500;
  --heading-4-medium-font-size: 28px;
  --heading-4-medium-letter-spacing: -0.56px;
  --heading-4-medium-line-height: 110.00000238418579%;
  --heading-4-medium-font-style: normal;
  --heading-4-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --heading-4-regular-font-weight: 400;
  --heading-4-regular-font-size: 28px;
  --heading-4-regular-letter-spacing: -0.56px;
  --heading-4-regular-line-height: 110.00000238418579%;
  --heading-4-regular-font-style: normal;
  --heading-4-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --heading-4-thin-font-weight: 300;
  --heading-4-thin-font-size: 28px;
  --heading-4-thin-letter-spacing: -0.56px;
  --heading-4-thin-line-height: 110.00000238418579%;
  --heading-4-thin-font-style: normal;
  --heading-5-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --heading-5-bold-font-weight: 700;
  --heading-5-bold-font-size: 24px;
  --heading-5-bold-letter-spacing: -0.48px;
  --heading-5-bold-line-height: 120.00000476837158%;
  --heading-5-bold-font-style: normal;
  --heading-5-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-5-semibold-font-weight: 500;
  --heading-5-semibold-font-size: 24px;
  --heading-5-semibold-letter-spacing: -0.48px;
  --heading-5-semibold-line-height: 120.00000476837158%;
  --heading-5-semibold-font-style: normal;
  --heading-5-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-5-medium-font-weight: 500;
  --heading-5-medium-font-size: 24px;
  --heading-5-medium-letter-spacing: -0.48px;
  --heading-5-medium-line-height: 120.00000476837158%;
  --heading-5-medium-font-style: normal;
  --heading-5-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --heading-5-regular-font-weight: 400;
  --heading-5-regular-font-size: 24px;
  --heading-5-regular-letter-spacing: -0.48px;
  --heading-5-regular-line-height: 120.00000476837158%;
  --heading-5-regular-font-style: normal;
  --heading-5-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --heading-5-thin-font-weight: 300;
  --heading-5-thin-font-size: 24px;
  --heading-5-thin-letter-spacing: -0.48px;
  --heading-5-thin-line-height: 120.00000476837158%;
  --heading-5-thin-font-style: normal;
  --heading-6-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --heading-6-bold-font-weight: 700;
  --heading-6-bold-font-size: 20px;
  --heading-6-bold-letter-spacing: -0.4px;
  --heading-6-bold-line-height: 120.00000476837158%;
  --heading-6-bold-font-style: normal;
  --heading-6-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-6-semibold-font-weight: 500;
  --heading-6-semibold-font-size: 20px;
  --heading-6-semibold-letter-spacing: -0.4px;
  --heading-6-semibold-line-height: 120.00000476837158%;
  --heading-6-semibold-font-style: normal;
  --heading-6-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --heading-6-medium-font-weight: 500;
  --heading-6-medium-font-size: 20px;
  --heading-6-medium-letter-spacing: -0.4px;
  --heading-6-medium-line-height: 120.00000476837158%;
  --heading-6-medium-font-style: normal;
  --heading-6-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --heading-6-regular-font-weight: 400;
  --heading-6-regular-font-size: 20px;
  --heading-6-regular-letter-spacing: -0.4px;
  --heading-6-regular-line-height: 120.00000476837158%;
  --heading-6-regular-font-style: normal;
  --heading-6-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --heading-6-thin-font-weight: 300;
  --heading-6-thin-font-size: 20px;
  --heading-6-thin-letter-spacing: -0.4px;
  --heading-6-thin-line-height: 120.00000476837158%;
  --heading-6-thin-font-style: normal;
  --body-1-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --body-1-bold-font-weight: 700;
  --body-1-bold-font-size: 18px;
  --body-1-bold-letter-spacing: -0.36px;
  --body-1-bold-line-height: 139.9999976158142%;
  --body-1-bold-font-style: normal;
  --body-1-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --body-1-semibold-font-weight: 500;
  --body-1-semibold-font-size: 18px;
  --body-1-semibold-letter-spacing: -0.36px;
  --body-1-semibold-line-height: 139.9999976158142%;
  --body-1-semibold-font-style: normal;
  --body-1-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --body-1-medium-font-weight: 500;
  --body-1-medium-font-size: 18px;
  --body-1-medium-letter-spacing: -0.36px;
  --body-1-medium-line-height: 139.9999976158142%;
  --body-1-medium-font-style: normal;
  --body-1-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --body-1-regular-font-weight: 400;
  --body-1-regular-font-size: 18px;
  --body-1-regular-letter-spacing: -0.36px;
  --body-1-regular-line-height: 139.9999976158142%;
  --body-1-regular-font-style: normal;
  --body-1-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --body-1-thin-font-weight: 300;
  --body-1-thin-font-size: 18px;
  --body-1-thin-letter-spacing: -0.36px;
  --body-1-thin-line-height: 139.9999976158142%;
  --body-1-thin-font-style: normal;
  --body-2-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --body-2-bold-font-weight: 700;
  --body-2-bold-font-size: 16px;
  --body-2-bold-letter-spacing: -0.32px;
  --body-2-bold-line-height: 139.9999976158142%;
  --body-2-bold-font-style: normal;
  --body-2-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --body-2-semibold-font-weight: 500;
  --body-2-semibold-font-size: 16px;
  --body-2-semibold-letter-spacing: -0.32px;
  --body-2-semibold-line-height: 139.9999976158142%;
  --body-2-semibold-font-style: normal;
  --body-2-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --body-2-regular-font-weight: 400;
  --body-2-regular-font-size: 16px;
  --body-2-regular-letter-spacing: -0.32px;
  --body-2-regular-line-height: 139.9999976158142%;
  --body-2-regular-font-style: normal;
  --body-2-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --body-2-thin-font-weight: 300;
  --body-2-thin-font-size: 16px;
  --body-2-thin-letter-spacing: -0.32px;
  --body-2-thin-line-height: 139.9999976158142%;
  --body-2-thin-font-style: normal;
  --caption-1-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --caption-1-bold-font-weight: 700;
  --caption-1-bold-font-size: 14px;
  --caption-1-bold-letter-spacing: -0.28px;
  --caption-1-bold-line-height: 139.9999976158142%;
  --caption-1-bold-font-style: normal;
  --caption-1-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --caption-1-semibold-font-weight: 500;
  --caption-1-semibold-font-size: 14px;
  --caption-1-semibold-letter-spacing: -0.28px;
  --caption-1-semibold-line-height: 139.9999976158142%;
  --caption-1-semibold-font-style: normal;
  --caption-1-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --caption-1-medium-font-weight: 500;
  --caption-1-medium-font-size: 14px;
  --caption-1-medium-letter-spacing: -0.28px;
  --caption-1-medium-line-height: 139.9999976158142%;
  --caption-1-medium-font-style: normal;
  --caption-1-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --caption-1-regular-font-weight: 400;
  --caption-1-regular-font-size: 14px;
  --caption-1-regular-letter-spacing: -0.28px;
  --caption-1-regular-line-height: 139.9999976158142%;
  --caption-1-regular-font-style: normal;
  --caption-1-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --caption-1-thin-font-weight: 300;
  --caption-1-thin-font-size: 14px;
  --caption-1-thin-letter-spacing: -0.28px;
  --caption-1-thin-line-height: 139.9999976158142%;
  --caption-1-thin-font-style: normal;
  --caption-2-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --caption-2-bold-font-weight: 700;
  --caption-2-bold-font-size: 12px;
  --caption-2-bold-letter-spacing: -0.12px;
  --caption-2-bold-line-height: normal;
  --caption-2-bold-font-style: normal;
  --caption-2-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --caption-2-semibold-font-weight: 500;
  --caption-2-semibold-font-size: 12px;
  --caption-2-semibold-letter-spacing: -0.12px;
  --caption-2-semibold-line-height: normal;
  --caption-2-semibold-font-style: normal;
  --caption-2-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --caption-2-medium-font-weight: 500;
  --caption-2-medium-font-size: 12px;
  --caption-2-medium-letter-spacing: -0.12px;
  --caption-2-medium-line-height: normal;
  --caption-2-medium-font-style: normal;
  --caption-2-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --caption-2-regular-font-weight: 400;
  --caption-2-regular-font-size: 12px;
  --caption-2-regular-letter-spacing: -0.12px;
  --caption-2-regular-line-height: normal;
  --caption-2-regular-font-style: normal;
  --caption-2-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --caption-2-thin-font-weight: 300;
  --caption-2-thin-font-size: 12px;
  --caption-2-thin-letter-spacing: -0.12px;
  --caption-2-thin-line-height: normal;
  --caption-2-thin-font-style: normal;
  --overline-1-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --overline-1-bold-font-weight: 700;
  --overline-1-bold-font-size: 12px;
  --overline-1-bold-letter-spacing: 1.44px;
  --overline-1-bold-line-height: normal;
  --overline-1-bold-font-style: normal;
  --overline-1-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --overline-1-semibold-font-weight: 500;
  --overline-1-semibold-font-size: 12px;
  --overline-1-semibold-letter-spacing: 1.44px;
  --overline-1-semibold-line-height: normal;
  --overline-1-semibold-font-style: normal;
  --overline-1-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --overline-1-medium-font-weight: 500;
  --overline-1-medium-font-size: 12px;
  --overline-1-medium-letter-spacing: 1.44px;
  --overline-1-medium-line-height: normal;
  --overline-1-medium-font-style: normal;
  --overline-1-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --overline-1-regular-font-weight: 400;
  --overline-1-regular-font-size: 12px;
  --overline-1-regular-letter-spacing: 1.44px;
  --overline-1-regular-line-height: normal;
  --overline-1-regular-font-style: normal;
  --overline-1-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --overline-1-thin-font-weight: 300;
  --overline-1-thin-font-size: 12px;
  --overline-1-thin-letter-spacing: 1.44px;
  --overline-1-thin-line-height: normal;
  --overline-1-thin-font-style: normal;
  --overline-2-bold-font-family: "SatoshiVariable-Bold", Helvetica;
  --overline-2-bold-font-weight: 700;
  --overline-2-bold-font-size: 10px;
  --overline-2-bold-letter-spacing: 1.2px;
  --overline-2-bold-line-height: normal;
  --overline-2-bold-font-style: normal;
  --overline-2-semibold-font-family: "SatoshiVariable-Medium", Helvetica;
  --overline-2-semibold-font-weight: 500;
  --overline-2-semibold-font-size: 10px;
  --overline-2-semibold-letter-spacing: 1.2px;
  --overline-2-semibold-line-height: normal;
  --overline-2-semibold-font-style: normal;
  --overline-2-medium-font-family: "SatoshiVariable-Medium", Helvetica;
  --overline-2-medium-font-weight: 500;
  --overline-2-medium-font-size: 10px;
  --overline-2-medium-letter-spacing: 1.2px;
  --overline-2-medium-line-height: normal;
  --overline-2-medium-font-style: normal;
  --overline-2-regular-font-family: "SatoshiVariable-Regular", Helvetica;
  --overline-2-regular-font-weight: 400;
  --overline-2-regular-font-size: 10px;
  --overline-2-regular-letter-spacing: 1.2px;
  --overline-2-regular-line-height: normal;
  --overline-2-regular-font-style: normal;
  --overline-2-thin-font-family: "SatoshiVariable-Light", Helvetica;
  --overline-2-thin-font-weight: 300;
  --overline-2-thin-font-size: 10px;
  --overline-2-thin-letter-spacing: 1.2px;
  --overline-2-thin-line-height: normal;
  --overline-2-thin-font-style: normal;
  --xs: 0px 1px 2px 0px rgba(16, 24, 40, 0.05);
  --sm: 0px 1px 2px 0px rgba(16, 24, 40, 0.06), 0px 1px 3px 0px rgba(16, 24, 40, 0.1);
  --md: 0px 2px 4px -2px rgba(16, 24, 40, 0.06), 0px 4px 8px -2px rgba(16, 24, 40, 0.1);
  --lg: 0px 4px 6px -2px rgba(16, 24, 40, 0.03), 0px 12px 16px -4px rgba(16, 24, 40, 0.08);
  --xl: 0px 8px 8px -4px rgba(16, 24, 40, 0.03), 0px 20px 24px -4px rgba(16, 24, 40, 0.08);
  --2xl: 0px 24px 48px -12px rgba(16, 24, 40, 0.18);
  --3xl: 0px 32px 64px -12px rgba(16, 24, 40, 0.14);
}

    </style>
  </head>
  <body>
    <div class="sign-up-step">
      <div class="div">
        <div class="frame">
          <div class="frame-2">
            <div class="frame-3">
              <div class="text-wrapper">STEP 3 OF 3</div>
              <div class="text-wrapper-2">Choose payment method</div>
              <div class="text-wrapper-3">Your payment is encrypted</div>
            </div>
            <div class="frame-4">
              <div class="frame-5">
                <div class="text-wrapper-4">E-Wallet</div>
                <div class="radio-button"><div class="radio-button-2"></div></div>
              </div>
              <div class="frame-5">
                <div class="text-wrapper-4">Credit/Debit Card</div>
                <div class="radio-button"><div class="radio-button-2"></div></div>
              </div>
              <div class="frame-5">
                <div class="text-wrapper-4">Bank Transfer</div>
                <div class="radio-button"><div class="radio-button-2"></div></div>
              </div>
            </div>
          </div>
          <button class="button"><div class="input-text">Next</div></button>
        </div>
        <header class="header">
          <div class="group">
            <div class="overlap-group"><div class="text-wrapper-5">A</div></div>
          </div>
          <button class="button-2"><div class="input-text-2">Login</div></button>
        </header>
      </div>
    </div>
  </body>
</html>
'''
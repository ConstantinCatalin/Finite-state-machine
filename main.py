import asyncio
import time
from random import randint


@asyncio.coroutine
def StartState():
    print("START: pornesti prima stare \n")
    input_value = randint(0, 1)
    time.sleep(1)
    if (input_value == 1):
        result = yield from State2(input_value)
    else:
        result = yield from State3(input_value)
    print("Rezumatul Tranzitiilor: \n\n Te trezesti dimineata si te pregatesti sa pleci la facultate \n" + result)


@asyncio.coroutine
def State2(transition_value):
    outputValue = str(("(Mergi pe ramura %s) Opresti alarma si te trezesti \n"
                        % (transition_value)))

    time.sleep(1)
    print("------Te pregatesti de plecare------")

    result = yield from State4(1)

    return (outputValue + str(result))


@asyncio.coroutine
def State3(transition_value):
    outputValue = str(("(Mergi pe ramura %s) Snooze inca 10 min \n"
                        % (transition_value)))
    time.sleep(1)
    print("------Ai dormit prea mult, te pregatesti in graba de plecare------")

    result = yield from State4(1)

    return (outputValue + str(result))


@asyncio.coroutine
def State4(transition_value):
    outputValue = str(("Esti gata de plecare  \n"))

    input_value = randint(0, 1)
    time.sleep(1)
    print("------Pleci de acasa------")
    if(input_value == 0):
        result = yield from State5(input_value)
    else:
        result = yield from State7(input_value)

    return (outputValue + str(result))


@asyncio.coroutine
def State5(transition_value):
    outputValue =  str(("(Mergi pe ramura %s) Vrei sa pleci cu masina \n" % (transition_value)))
    input_value = randint(0, 2)
    time.sleep(1)
    print("------Urci in masina------")
    if(input_value == 0):
        result = yield from State6(input_value)
    if(input_value == 1):
        print("------Masina nu porneste------")
        result = yield from State7(input_value)
    if(input_value == 2):
        print("------Ai uitat ceva acasa------")
        result = yield from State4(input_value)
    return (outputValue + str(result))


@asyncio.coroutine
def State6(transition_value):
    outputValue = str(("Parchezi masina  \n"))

    time.sleep(1)
    print("------Esti in parcare------")

    result = yield from State13(1)

    return (outputValue + str(result))


@asyncio.coroutine
def State7(transition_value):
    outputValue =  str(("(Mergi pe ramura %s) Mergi in statia de autobuz \n" % (transition_value)))
    input_value = randint(0, 1)
    time.sleep(1)

    print("------Astepti autobuzul------")

    if(input_value == 0):
        result = yield from State8(input_value)
    else:
        result = yield from State4(input_value)

    return (outputValue + str(result))

@asyncio.coroutine
def State8(transition_value):
    outputValue = str(("A venit autobuzul \n"))

    input_value = randint(0, 1)
    time.sleep(1)
    print("------Urci in autobuz------")

    if(input_value == 0):
        result = yield from State9(input_value)
    else:
        result = yield from State10(input_value)

    return (outputValue + str(result))


@asyncio.coroutine
def State9(transition_value):
    outputValue = str(("(Mergi pe ramura %s) Cumperi un bilet \n" % (transition_value)))

    time.sleep(1)
    print("------Ai luat un bilet------")
    result = yield from State11(1)

    return (outputValue + str(result))


@asyncio.coroutine
def State10(transition_value):
    outputValue = str(("(Mergi pe ramura %s) Ai un bilet in buzunar \n" % (transition_value)))

    time.sleep(1)
    print("------Scoti biletul din buzunar------")
    result = yield from State11(1)

    return (outputValue + str(result))


@asyncio.coroutine
def State11(transition_value):
    outputValue = str(("Mergi la validator \n"))

    time.sleep(1)
    print("------Validezi biletul------")
    result = yield from State12(1)
    return (outputValue + str(result))


@asyncio.coroutine
def State12(transition_value):
    outputValue = str(("Mergi 9 statii \n" ))

    time.sleep(1)
    print("------Cobori din autobuz------")
    result = yield from State13(1)
    return (outputValue + str(result))


@asyncio.coroutine
def State13(transition_value):
    outputValue = str(("Intri in clasa \n"))
    time.sleep(1)

    result = yield from EndState(1)

    return (outputValue + str(result))


@asyncio.coroutine
def EndState(transition_value):
    outputValue = str(("Bravo, ai ajuns la timp la facultate! \n"))

    print("STOP: ----------------")
    return (outputValue)


if __name__ == "__main__":
    print("--------MSF-----------")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(StartState())
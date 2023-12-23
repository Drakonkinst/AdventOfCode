import sys, os, itertools as itt
from collections import deque # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

class Module:
    def is_state_reset(self):
        return True
    
    # Return True to send high pulse, False to send low pulse, or None to send no pulse
    def receive_pulse(self, name, isHigh):
        return isHigh

class FlipFlop(Module):
    
    def __init__(self):
        self.state = False
    
    def is_state_reset(self):
        return self.state == False
    
    def receive_pulse(self, name, isHigh):
        if (isHigh):
            return None
        self.state = not self.state
        return self.state
    
class Conjunction(Module):
    
    def __init__(self):
        self.inputs = {}
    
    def set_inputs(self, inputs):
        self.inputs = {}
        for inputName in inputs:
            self.inputs[inputName] = False
    
    def is_state_reset(self):
        return all(memory == False for memory in self.inputs.values())
    
    def receive_pulse(self, name, isHigh):
        self.inputs[name] = isHigh
        if all(memory == True for memory in self.inputs.values()):
            return False
        return True
    
def main():
    nodes = {}
    inputs = {}
    outputs = {}
    
    # Parse input into modules
    for line in lines:
        signature, outputStr = [s.strip() for s in line.split("->")]
        name = None
        if signature.startswith("%"):
            name = signature[1:]
            nodes[name] = FlipFlop()
        elif signature.startswith("&"):
            name = signature[1:]
            nodes[name] = Conjunction()
        else:
            name = signature
            # Default module acts as a broadcaster
            nodes[signature] = Module()
        
        # In case no outputs
        if not outputStr:
            continue
        
        outputs[name] = outputStr.split(", ")
        for output in outputs[name]:
            if output not in inputs:
                inputs[output] = []
            inputs[output].append(name)
    
    # Retroactively set inputs now that all modules have been parsed
    for name, module in nodes.items():
        if isinstance(module, Conjunction):
            module.set_inputs(inputs[name])
    
    pushCount = 0
    
    # rx's only input should be a single conjunction node with n inputs
    endInputs = inputs[inputs["rx"][0]]
    # rx will receive a low signal when ALL of endInputs receive a low signal in the same press
    # So figure out each of those and LCM the result
    endLowCycle = {endInput: None for endInput in endInputs}
    
    while any(x is None for x in endLowCycle.values()):
        pushCount += 1
        # Push the button!
        pulses = deque()
        pulses.append(("broadcaster", "button", False))
        while pulses:
            (receiver, sender, isHigh) = pulses.popleft()
            if not isHigh and receiver in endLowCycle:
                endLowCycle[receiver] = pushCount
            if receiver not in nodes:
                continue
            module = nodes[receiver]
            result = module.receive_pulse(sender, isHigh)
            if result is not None:
                for output in outputs[receiver]:
                    pulses.append((output, receiver, result))
        if all(node.is_state_reset() for node in nodes.values()):
            assert False
    
    print(math.lcm(*endLowCycle.values()))

if __name__ == "__main__":
    main()
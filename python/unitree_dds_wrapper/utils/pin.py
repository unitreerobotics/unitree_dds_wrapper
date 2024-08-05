import pinocchio as pin
import numpy as np

def BuildReducedModel(model, jointsToLock):
    jointsToLockIDs = []
    for jn in jointsToLock:
        if model.existJointName(jn):
            jointsToLockIDs.append(model.getJointId(jn))
        else:
            print('Joint ' + jn + ' not found in the model.')
    model_reduced = pin.buildReducedModel(model, jointsToLockIDs, np.zeros(model.nq))
    return pin.RobotWrapper(model_reduced)
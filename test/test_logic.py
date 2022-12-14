from src.logic.git_automatization import git_add, git_commit, git_push

def test_subprocess():

    assert git_add() == 0
    assert git_commit() == 0
    assert git_push() == 0
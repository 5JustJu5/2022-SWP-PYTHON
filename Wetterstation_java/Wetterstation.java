public interface Wetterstation {
	public abstract void addBeobachter(Bildschirme beobachter);
	public abstract void removeBeobachter(Bildschirme beobachter);
	public abstract void notifyAlleBeobachter();
}